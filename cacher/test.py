import time

from . import lru_cache


def fib(n: int) -> int:
    return n if n < 2 else fib(n - 1) + fib(n - 2)


@lru_cache(10)
def fib_cached(n: int) -> int:
    return n if n < 2 else fib_cached(n - 1) + fib_cached(n - 2)


if __name__ == "__main__":
    for i in range(1, 100_000):
        start = time.time()
        r = fib_cached(i)
        end = time.time()
        print(f"fib({i}) in {end - start} seconds")
