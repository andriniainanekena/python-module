#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = name
        self._height: float = 0.0
        self._age: int = 0
        self._growth_rate: float = 0.8

        if height < 0:
            print(
                f"{self._name.capitalize()}: Error, height can't be negative"
            )
        else:
            self._height = float(height)

        if age < 0:
            print(
                f"{self._name.capitalize()}: Error, age can't be negative"
            )
        else:
            self._age = age

    def show(self) -> None:
        print(
            f"{self._name.capitalize()}: {self._height:.1f}cm,"
            f" {self._age} days old"
        )

    def grow(self) -> None:
        self._height = round(self._height + self._growth_rate, 2)

    def age_one_day(self) -> None:
        self._age += 1

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, value: float) -> None:
        if value < 0:
            print(
                f"{self._name.capitalize()}: Error, height can't be negative"
            )
            print("Height update rejected")
        else:
            self._height = float(value)
            print(f"Height updated: {int(value)}cm")

    def set_age(self, value: int) -> None:
        if value < 0:
            print(
                f"{self._name.capitalize()}: Error, age can't be negative"
            )
            print("Age update rejected")
        else:
            self._age = value
            print(f"Age updated: {value} days")


if __name__ == "__main__":
    print("=== Garden Security System ===")

    rose = Plant("Rose", 15.0, 10)

    print("Plant created: ", end="")
    rose.show()

    rose.set_height(25)
    rose.set_age(30)

    rose.set_height(-5)
    rose.set_age(-1)

    print("Current state: ", end="")
    rose.show()
