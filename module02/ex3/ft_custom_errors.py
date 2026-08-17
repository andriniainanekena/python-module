#!/usr/bin/env python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    def __init__(self, *args: str) -> None:
        super().__init__(*args or ("Unknown plant error",))


class WaterError(GardenError):
    def __init__(self, *args: str) -> None:
        super().__init__(*args or ("Unknown water error",))


def raise_plant_error() -> None:
    raise PlantError("The tomato plant is wilting!")


def raise_water_error() -> None:
    raise WaterError("Not enough water in the tank!")


def ft_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("Testing PlantError...")
    try:
        raise_plant_error()
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e}")

    print()
    print("Testing WaterError...")
    try:
        raise_water_error()
    except WaterError as e:
        print(f"Caught {e.__class__.__name__}: {e}")

    print()
    print("Testing catching all garden errors...")
    try:
        raise_plant_error()
    except GardenError as e:
        print(f"Caught {e.__class__.__name__}: {e}")

    try:
        raise_water_error()
    except GardenError as e:
        print(f"Caught {e.__class__.__name__}: {e}")

    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    ft_custom_errors()
