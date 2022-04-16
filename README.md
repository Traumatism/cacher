# cacher 🧳
## A lightweight cache library for Python

## Installation

- Clone the repo
- Run `python setup.py install`

## Usage

```python
import cacher
import time


@cacher.lru_cache
def expensive_function(x):
    print("processing function")
    time.sleep(1)
    return x * x


@cacher.async_lru_cache
async def expensive_async_function(x):
    print("processing function")
    time.sleep(1)
    return x * x


def expensive_function_b(x):
    print("processing function")
    time.sleep(1)
    return x * x


lrued_function = cacher.lru_cache(expensive_function)
lrued_function(x=2)  # keyword arguments support
```
