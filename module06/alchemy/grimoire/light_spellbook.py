def light_spell_allowed_ingredients() -> list[str]:
    return ['earth', 'air', 'fire', 'water']


def light_spell_record(spell_name: str, ingredients: str) -> str:
    import alchemy.grimoire.light_validator as light_validator
    result = light_validator.validate_ingredients(ingredients)
    if result.startswith('VALID'):
        return (
            f'Spell recorded: {spell_name}'
            f' (Earth, wind and fire - VALID)'
        )
    return f'Spell rejected: {spell_name} - invalid ingredients'
