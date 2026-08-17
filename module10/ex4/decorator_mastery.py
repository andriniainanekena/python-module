import time
from collections.abc import Callable
from functools import wraps
from typing import Any, Protocol


class _CodeObject(Protocol):
    co_varnames: tuple[str, ...]
    co_argcount: int


class _IntrospectableSpell(Protocol):
    __code__: _CodeObject

    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {wrapper.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable[..., Any]:

    def decorator(func: _IntrospectableSpell) -> Callable[..., Any]:
        varnames = func.__code__.co_varnames[: func.__code__.co_argcount]
        power_index = varnames.index("power")

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if "power" in kwargs:
                power: int = kwargs["power"]
            else:
                power = args[power_index]
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable[..., Any]:

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == max_attempts:
                        break
                    print(
                        f"Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})"
                    )
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(
            char.isalpha() or char == " " for char in name
        )

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball(target: str) -> str:
    time.sleep(0.1)
    return "Fireball cast!"


@retry_spell(max_attempts=3)
def unstable_spell() -> str:
    raise RuntimeError("The weave unravels")


def main() -> None:
    print("Testing spell timer...")
    result = fireball("Dragon")
    print(f"Result: {result}")

    print("\nTesting retrying spell...")
    print(unstable_spell())
    print("Waaaaaaagh spelled !")

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Alex"))
    print(MageGuild.validate_mage_name("A1"))
    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))


if __name__ == "__main__":
    main()
