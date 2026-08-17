from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = light_spell_allowed_ingredients()
    if any(i in ingredients.lower() for i in allowed):
        return f'VALID - {ingredients}'
    return f'INVALID - {ingredients}'
