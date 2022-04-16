import functools

from typing import (
    Any,
    Callable,
    Coroutine,
    TypeVar,
    ParamSpec,
    Dict,
)

__all__ = (
    "lru_cache", "async_lru_cache"
)

T = TypeVar("T")
P = ParamSpec("P")


def lru_cache(func: Callable[P, T]) -> Callable[P, T]:
    """ LRU cache decorator. """

    cache: Dict[int, T] = {}

    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        key = hash((
            args,
            frozenset(kwargs.items())  # type: ignore
        ))

        if key not in cache:

            if len(cache) == 128:
                cache.pop(next(iter(cache)))

            cache[key] = func(*args, **kwargs)

        return cache[key]

    return wrapper


def async_lru_cache(
    func: Callable[P, Coroutine[Any, Any, T]]
) -> Callable[P, Coroutine[Any, Any, T]]:
    """ LRU cache decorator for async functions. """

    cache: Dict[int, T] = {}

    @functools.wraps(func)
    async def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        key = hash((
            args,
            frozenset(kwargs.items())  # type: ignore
        ))

        if key not in cache:

            if len(cache) == 128:
                cache.pop(next(iter(cache)))

            cache[key] = await func(*args, **kwargs)

        return cache[key]

    return wrapper
