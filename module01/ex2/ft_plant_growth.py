#!/usr/bin/env python3

class Plant:
    def __init__(self) -> None:
        self.name: str = ""
        self.height: float = 0.0
        self.age: int = 0
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
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose.age = 30
    rose.growth_rate = 0.8

    print("=== Garden Plant Growth ===")
    rose.show()

    initial_height: float = rose.height

    for day in range(1, 8):
        rose.grow()
        rose.age_one_day()
        print(f"=== Day {day} ===")
        rose.show()

    total_growth = round(rose.height - initial_height, 2)
    print(f"Growth this week: {total_growth}cm")
