import pytest
from toolkit.core import flatten_dict, deep_merge, slugify, chunk_list, Timer, memoize

def test_flatten_dict():
    nested = {'a': {'b': {'c': 1}}, 'd': 2}
    expected = {'a.b.c': 1, 'd': 2}
    assert flatten_dict(nested) == expected

def test_deep_merge():
    a = {'x': 1, 'nested': {'y': 2}}
    b = {'nested': {'z': 3}}
    merged = deep_merge(a, b)
    assert merged['nested'] == {'y': 2, 'z': 3}

def test_slugify():
    assert slugify(" Hello, World! ") == "hello-world"

def test_chunk_list():
    data = list(range(7))
    chunks = list(chunk_list(data, 3))
    assert chunks == [[0,1,2], [3,4,5], [6]]

def test_timer():
    with Timer() as t:
        sum(range(100000))
    assert t.interval > 0

def test_memoize():
    calls = []
    @memoize
    def fib(n):
        calls.append(n)
        return 1 if n < 2 else fib(n-1) + fib(n-2)
    assert fib(10) == 89
    assert len(calls) < 20