#!/usr/bin/env python3
"""
Advanced potion recipes for the alchemy package.
"""

from .elements import create_fire, create_water, create_earth, create_air


def healing_potion():
    return (
        "Healing potion brewed with "
        f"{create_fire()} and {create_water()}"
    )


def strength_potion():
    return (
        "Strength potion brewed with "
        f"{create_earth()} and {create_fire()}"
    )


def invisibility_potion():
    return (
        "Invisibility potion brewed with "
        f"{create_air()} and {create_water()}"
    )


def wisdom_potion():
    elements = (
        f"{create_fire()}, "
        f"{create_water()}, "
        f"{create_earth()}, "
        f"{create_air()}"
    )
    return f"Wisdom potion brewed with all elements: {elements}"
