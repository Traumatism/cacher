# cacher 🧳
## A lightweight cache library for Python

## Installation

- Clone the repo
- Run `python setup.py install`

## Usage

```python
import cacher
import time

@cacher.lru_cache  # Cache with 128 values
def expensive_function(x):
    print("processing function a")
    time.sleep(1)
    return x * x

@cacher.lru_cache(1024)  # Cache with 1024 values
def expensive_function_b(x):
    print("processing function b")
    time.sleep(1)
    return x * x

def expensive_function_c(x):
    print("processing function c")
    time.sleep(1)
    return x * x

lrued_function = cacher.lru_cache(expensive_function_c)
lrued_function(x=2)  # keyword arguments support
```
