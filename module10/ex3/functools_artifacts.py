import operator
from collections.abc import Callable
from functools import lru_cache, partial, reduce, singledispatch
from typing import Any


def _spell_max(left: int, right: int) -> int:
    return left if left > right else right


def _spell_min(left: int, right: int) -> int:
    return left if left < right else right


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    operator_handlers: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": _spell_max,
        "min": _spell_min,
    }
    if operation not in operator_handlers:
        raise ValueError(f"Unknown operation: {operation}")
    return reduce(operator_handlers[operation], spells)


def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str],
) -> dict[str, Callable[[str], str]]:
    return {
        "fire_enchant": partial(base_enchantment, 50, "fire"),
        "ice_enchant": partial(base_enchantment, 50, "ice"),
        "shadow_enchant": partial(base_enchantment, 50, "shadow"),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


@singledispatch
def _cast(spell: Any) -> str:
    return "Unknown spell type"


@_cast.register
def _cast_int(spell: int) -> str:
    return f"{spell} damage"


@_cast.register
def _cast_str(spell: str) -> str:
    return spell


@_cast.register(list)
def _cast_list(spell: list[Any]) -> str:
    return f"{len(spell)} spells"


def spell_dispatcher() -> Callable[[Any], str]:
    return _cast


def enchant_item(power: int, element: str, target: str) -> str:
    return f"{element} {target}"


def main() -> None:
    print("Testing spell reducer...")
    powers = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(powers, 'add')}")
    print(f"Product: {spell_reducer(powers, 'multiply')}")
    print(f"Max: {spell_reducer(powers, 'max')}")
    try:
        spell_reducer(powers, "divide")
    except ValueError as error:
        print(f"Reducer error handled: {error}")

    print("\nTesting partial enchanter...")
    enchanters = partial_enchanter(enchant_item)
    print(enchanters["fire_enchant"]("Sword"))
    print(enchanters["ice_enchant"]("Shield"))
    print(enchanters["shadow_enchant"]("Cloak"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print(f"Fib(15) again (cached): {memoized_fibonacci(15)}")
    print(memoized_fibonacci.cache_info())

    print("\nTesting spell dispatcher...")
    dispatch = spell_dispatcher()
    print(f"Damage spell: {dispatch(42)}")
    print(f"Enchantment: {dispatch('fireball')}")
    print(f"Multi-cast: {dispatch([1, 2, 3])}")
    print(f"Unknown type: {dispatch(3.14)}")


if __name__ == "__main__":
    main()
