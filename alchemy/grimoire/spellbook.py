#!/usr/bin/env python3
"""
Spell recording logic.
"""


def record_spell(spell_name: str, ingredients: str) -> str:
    """
    Record a spell only if ingredients validation is successful.
    Uses a late import to avoid circular dependency.
    """
    from .validator import validate_ingredients  # late import

    validation_result = validate_ingredients(ingredients)

    if validation_result.endswith(" - VALID"):
        return f"Spell recorded: {spell_name} ({validation_result})"

    return f"Spell rejected: {spell_name} ({validation_result})"
