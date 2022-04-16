# cacher 🧳
## A lightweight cache library for Python

## Installation

- Clone the repo
- Run `python setup.py install`

## Usage

```python
import cacher


@cacher.lru_cache
def expensive_function(x):
    return x * x


@cacher.async_lru_cache
async def expensive_async_function(x):
    return x * x

```
