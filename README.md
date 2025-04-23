# Toolkit

A compact, well-documented collection of Python utility functions and tools, ready to drop into your projects.

## Features

- `flatten_dict` – Recursively flatten a nested dictionary
- `deep_merge` – Merge two dictionaries deeply
- `slugify` – Create URL-friendly slugs from strings
- `retry` – Decorator to retry failing functions
- `chunk_list` – Split lists into chunks
- `Timer` – Context manager for timing code
- `memoize` – Simple memoization decorator

## Installation

```bash
pip install .
```

## Testing

```bash
pytest
```

## Example Usage

```python
from toolkit.core import slugify, flatten_dict

print(slugify("Hello, World!"))  # Output: hello-world
print(flatten_dict({'a': {'b': 1}}))  # Output: {'a.b': 1}
```