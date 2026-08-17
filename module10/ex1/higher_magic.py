from collections.abc import Callable


def spell_combiner(
    spell1: Callable[[str, int], str], spell2: Callable[[str, int], str]
) -> Callable[[str, int], tuple[str, str]]:

    def combined(target: str, power: int) -> tuple[str, str]:
        return spell1(target, power), spell2(target, power)

    return combined


def power_amplifier(
    base_spell: Callable[[str, int], str], multiplier: int
) -> Callable[[str, int], str]:

    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplified


def conditional_caster(
    condition: Callable[[str, int], bool],
    spell: Callable[[str, int], str],
) -> Callable[[str, int], str]:

    def maybe_cast(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return maybe_cast


def spell_sequence(
    spells: list[Callable[[str, int], str]],
) -> Callable[[str, int], list[str]]:

    def cast_all(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]

    return cast_all


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target}"


def heal(target: str, power: int) -> str:
    return f"Heals {target}"


def power_spell(target: str, power: int) -> str:
    return f"Power increases {power}"


def main() -> None:
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    fire_result, heal_result = combined("Dragon", 20)
    print(f"Combined spell result: {fire_result}, {heal_result}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    original = 10
    result = mega_fireball("Dragon", original)
    print(f"Original: {original}, Amplified: {original * 3}")
    print(f"Result: {result}")

    print("\nTesting conditional caster...")
    guarded_fireball = conditional_caster(
        lambda target, power: power >= 15,
        fireball,
    )
    print(guarded_fireball("Dragon", 20))
    print(guarded_fireball("Dragon", 5))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal, power_spell])
    results = sequence("Dragon", 20)
    for result in results:
        print(result)

    print("\nTesting callable()...")
    print(f"Is fireball callable? {callable(fireball)}")


if __name__ == "__main__":
    main()
