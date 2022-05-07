from typing import Callable, TypeVar, ParamSpec, Dict

T = TypeVar("T")
P = ParamSpec("P")


def generate_wrapper(size: int, func: Callable[P, T]) -> Callable[P, T]:
    """Generate wrapper"""

    cache: Dict[int, T] = {}

    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        key = hash((args, frozenset(kwargs.items())))  # type: ignore

        if key in cache:
            return cache[key]

        if len(cache) == size and size != -1:
            cache.pop(next(iter(cache)))

        cache[key] = r = func(*args, **kwargs)
        return r

    return wrapper
