"""Read-only inspection of DDLC archive ASTs; never imports game code."""
import argparse
import io
import json
import pickle
import struct
import zlib
from pathlib import Path


class Node:
    def __new__(cls, *args):
        obj = object.__new__(cls)
        obj.args = args
        return obj

    def __init__(self, *args):
        self.args = args

    def __setstate__(self, state):
        self.state = state
        if isinstance(state, dict):
            self.__dict__.update(state)
        elif isinstance(state, tuple):
            for item in state:
                if isinstance(item, dict):
                    self.__dict__.update(item)


TYPES = {}


class Reader(pickle.Unpickler):
    def find_class(self, module, name):
        key = (module, name)
        if key not in TYPES:
            TYPES[key] = type(name, (Node,), {'module': module})
        return TYPES[key]


def archive(path):
    data = Path(path).read_bytes()
    header = data.split(b'\n', 1)[0].split()
    offset, key = int(header[1], 16), int(header[2], 16)
    index = Reader(io.BytesIO(zlib.decompress(data[offset:])), encoding='latin1').load()
    for name, chunks in sorted(index.items()):
        parts = []
        for chunk in chunks:
            start, length = chunk[0] ^ key, chunk[1] ^ key
            prefix = chunk[2] if len(chunk) == 3 else b''
            if isinstance(prefix, str):
                prefix = prefix.encode('latin1')
            parts.append((prefix or b'') + data[start:start + length - len(prefix or b'')])
        yield name, b''.join(parts)


def ast(data):
    slots = {}
    if data.startswith(b'RENPY RPC2'):
        pos = 10
        while True:
            slot, start, length = struct.unpack_from('<III', data, pos)
            pos += 12
            if slot == 0:
                break
            slots[slot] = data[start:start + length]
        data = slots.get(2, slots[1])
    return Reader(io.BytesIO(zlib.decompress(data)), encoding='latin1').load()


def walk(value, path='', seen=None):
    if seen is None:
        seen = set()
    if isinstance(value, (Node, list, tuple, dict)):
        if id(value) in seen:
            return
        seen.add(id(value))
    yield path, value
    if isinstance(value, Node):
        for k, v in value.__dict__.items():
            if k not in ('next', 'state'):
                yield from walk(v, path + '.' + k, seen)
        if type(value).__name__ == 'PyCode':
            yield from walk(getattr(value, 'state', None), path + '.state', seen)
    elif isinstance(value, dict):
        for k, v in value.items():
            yield from walk(v, path + '[' + str(k) + ']', seen)
    elif isinstance(value, (list, tuple)):
        for i, v in enumerate(value):
            yield from walk(v, path + '[' + str(i) + ']', seen)


def inspect(source, output):
    output.mkdir(parents=True, exist_ok=True)
    records = []
    counts = {}
    for name, data in archive(source):
        if not name.endswith('.rpyc'):
            continue
        root = ast(data)
        modules = []
        for path, value in walk(root):
            if isinstance(value, Node):
                cls = type(value).__name__
                counts[cls] = counts.get(cls, 0) + 1
                if cls in ('Say', 'Translate', 'Menu', 'SLDisplayable', 'PyCode', 'UserStatement', 'Define', 'Default'):
                    def simple(x):
                        if isinstance(x, Node):
                            if type(x).__name__ == 'PyExpr':
                                return x.args
                            return '<' + type(x).__name__ + '>'
                        if isinstance(x, (list, tuple)):
                            return [simple(a) for a in x]
                        if isinstance(x, dict):
                            return {str(k): simple(v) for k, v in x.items()}
                        if isinstance(x, bytes):
                            return repr(x)
                        if isinstance(x, type):
                            return '<class ' + x.__name__ + '>'
                        return x
                    fields = {k: simple(v) for k, v in value.__dict__.items() if k not in ('next','block','children','state')}
                    if cls == 'PyCode':
                        fields['state'] = simple(value.state)
                    modules.append({'class':cls, 'path':path, 'fields':fields})
            if isinstance(value, str):
                records.append({'module':name, 'path':path, 'text':value})
        (output / (name + '.json')).write_text(json.dumps(modules, ensure_ascii=False, indent=2), encoding='utf-8')
    (output / 'strings.json').write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(counts, indent=2))


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('archive')
    p.add_argument('output', type=Path)
    a = p.parse_args()
    inspect(a.archive, a.output)
