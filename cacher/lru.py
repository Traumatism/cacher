from typing import Callable, TypeVar, ParamSpec, overload, Union

from .wrap import generate_wrapper


__all__ = ("lru_cache",)

T = TypeVar("T")
P = ParamSpec("P")


@overload
def lru_cache(size: int) -> Callable[[Callable[P, T]], Callable[P, T]]:
    """Overload for custom size cache"""
    ...


@overload
def lru_cache(size: Callable[P, T]) -> Callable[P, T]:
    """Overload for default size cache"""
    ...


def lru_cache(
    size: Union[int, Callable[P, T]]
) -> Union[Callable[P, T], Callable[[Callable[P, T]], Callable[P, T]]]:
    """LRU cache decorator"""

    if not isinstance(size, int):
        function = size
        return generate_wrapper(function)

    if size < 1 and size != -1:
        raise ValueError(
            "Cache size must be greater than 0 (use -1 for infinite cache)"
        )

    return lambda func: (generate_wrapper(func, size))
