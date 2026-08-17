from ex0.creature import Creature
from ex1 import (
    HealingCreatureFactory,
    TransformCreatureFactory,
    HealCapability,
    TransformCapability,
)


def test_healing_factory() -> None:
    print("Testing Creature with healing capability")
    factory = HealingCreatureFactory()

    for label in ("base", "evolved"):
        if label == "base":
            c: Creature = factory.create_base()
        else:
            c = factory.create_evolved()
        print(f" {label}:")
        print(c.describe())
        print(c.attack())
        if isinstance(c, HealCapability):
            print(c.heal())


def test_transform_factory() -> None:
    print("Testing Creature with transform capability")
    factory = TransformCreatureFactory()

    for label in ("base", "evolved"):
        if label == "base":
            c = factory.create_base()
        else:
            c = factory.create_evolved()
        print(f" {label}:")
        print(c.describe())
        print(c.attack())
        if isinstance(c, TransformCapability):
            print(c.transform())
            print(c.attack())
            print(c.revert())


if __name__ == "__main__":
    test_healing_factory()
    print()
    test_transform_factory()
