import alchemy.grimoire.dark_validator as dark_validator


def dark_spell_allowed_ingredients() -> list[str]:
    return ['bats', 'frogs', 'arsenic', 'eyeball']


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    result = dark_validator.validate_ingredients(ingredients)
    if result.startswith('VALID'):
        return (
            f'Spell recorded: {spell_name}'
            f' (Earth, wind and fire - VALID)'
        )
    return 'Error somewhere'
