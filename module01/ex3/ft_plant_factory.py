#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age
        self.growth_rate: float = 0.8

    def show(self) -> None:
        print(
            f"{self.name.capitalize()}: {self.height}cm, {self.age} days old"
        )

    def grow(self) -> None:
        self.height = round(self.height + self.growth_rate, 2)

    def age_one_day(self) -> None:
        self.age += 1


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120),
    ]

    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end="")
        plant.show()
