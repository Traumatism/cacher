import time

from . import lru_cache


def fib(n: int) -> int:
    return n if n < 2 else fib(n - 1) + fib(n - 2)


def fib_cached(n: int) -> int:
    return n if n < 2 else fib_cached(n - 1) + fib_cached(n - 2)


if __name__ == "__main__":
    f = lru_cache(fib)

    for i in range(100_000):

        start = time.time()
        f(i)
        end = time.time()

        print(f"fib({i}) in {end - start} seconds")
