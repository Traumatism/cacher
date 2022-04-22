import functools

from typing import (
    Callable, TypeVar, ParamSpec, Dict, overload, Union
)

__all__ = ("lru_cache", )

T = TypeVar("T")
P = ParamSpec("P")


def generate_wrapper(size: int, func: Callable[P, T]) -> Callable[P, T]:
    """ Generate wrapper """

    cache: Dict[int, T] = dict()

    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        key = hash((args, frozenset(kwargs.items())))  # type: ignore

        if key in cache:
            return cache[key]

        if len(cache) == size and size != -1:
            cache.pop(next(iter(cache)))

        r = func(*args, **kwargs)

        cache[key] = r

        return r

    return wrapper


@overload
def lru_cache(size: int) -> Callable[[Callable[P, T]], Callable[P, T]]:
    """ Overload for custom size cache """
    ...


@overload
def lru_cache(size: Callable[P, T]) -> Callable[P, T]:
    """ Overload for default size cache """
    ...


def lru_cache(
    size: Union[int, Callable[P, T]]
) -> Union[Callable[P, T], Callable[[Callable[P, T]], Callable[P, T]]]:
    """ LRU cache decorator """

    if not isinstance(size, int):
        return generate_wrapper(128, size)

    _size: int = size

    if _size < 1 and _size != -1:
        raise ValueError(
            "Cache size must be greater than 0 (use -1 for infinite cache)"
        )

    return lambda func: (generate_wrapper(_size, func))
