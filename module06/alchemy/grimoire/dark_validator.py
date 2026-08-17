from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    if ingredients in dark_spell_allowed_ingredients():
        return f'VALID - {ingredients}'
    return f'INVALID - {ingredients}'
