import re
import time
from functools import wraps
from typing import Any, Callable, Dict, Generator, List, Tuple, TypeVar

T = TypeVar("T")


def flatten_dict(d: Dict[Any, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else str(k)
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def deep_merge(a: Dict[Any, Any], b: Dict[Any, Any]) -> Dict[Any, Any]:
    result = a.copy()
    for k, v in b.items():
        if k in result and isinstance(result[k], dict) and isinstance(v, dict):
            result[k] = deep_merge(result[k], v)
        else:
            result[k] = v
    return result


def slugify(text: str, separator: str = '-') -> str:
    text = re.sub(r'[^\w\s-]', '', text).strip().lower()
    return re.sub(r'[\s_-]+', separator, text)


def retry(retries: int = 3, delay: float = 1.0, exceptions: Tuple[type, ...] = (Exception,)) -> Callable:
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> T:
            last_exc = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exc = e
                    if attempt < retries - 1:
                        time.sleep(delay)
            raise last_exc
        return wrapper
    return decorator


def chunk_list(data: List[T], size: int) -> Generator[List[T], None, None]:
    for i in range(0, len(data), size):
        yield data[i:i + size]


class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args):
        self.end = time.perf_counter()
        self.interval = self.end - self.start

    def __str__(self):
        return f"{self.interval:.4f}s"


def memoize(func: Callable[..., T]) -> Callable[..., T]:
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper