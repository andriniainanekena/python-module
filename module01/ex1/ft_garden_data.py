#!/usr/bin/env python3

class Plant:
    def __init__(self) -> None:
        self.name: str = ""
        self.height: float = 0.0
        self.age: int = 0

    def show(self) -> None:
        print(
            f"{self.name.capitalize()}: "
            f"{self.height}cm, {self.age} days old"
        )


if __name__ == "__main__":
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25
    rose.age = 30

    sunflower = Plant()
    sunflower.name = "Sunflower"
    sunflower.height = 80
    sunflower.age = 45

    cactus = Plant()
    cactus.name = "Cactus"
    cactus.height = 15
    cactus.age = 120

    plants = [rose, sunflower, cactus]

    print("=== Garden Plant Registry ===")
    for plant in plants:
        plant.show()
