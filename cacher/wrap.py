import functools

from typing import Callable, ParamSpec, TypeVar, Dict

T = TypeVar("T")
P = ParamSpec("P")


def generate_wrapper(size: int, func: Callable[P, T]) -> Callable[P, T]:
    """Generate wrapper"""

    cache: Dict[int, T] = {}

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
