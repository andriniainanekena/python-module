#!/usr/bin/env python3

class Plant:
    class _Stats:
        def __init__(self) -> None:
            self._grows: int = 0
            self._ages: int = 0
            self._shows: int = 0

        def record_grow(self) -> None:
            self._grows += 1

        def record_age(self) -> None:
            self._ages += 1

        def record_show(self) -> None:
            self._shows += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grows} grow, "
                f"{self._ages} age, "
                f"{self._shows} show"
            )

    def __init__(
        self,
        name: str,
        height: float = 0.0,
        days: int = 0,
        growth_rate: float = 0.8
    ) -> None:
        self.name = name
        self._height: float = max(0.0, height)
        self._days: int = max(0, days)
        self._growth_rate = growth_rate
        self._stats: Plant._Stats = Plant._Stats()

    @staticmethod
    def is_older_than_a_year(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def get_height(self) -> float:
        return self._height

    def set_height(self, value: float) -> bool:
        if value < 0:
            print(f"{self.name}: Error, height can't be negative")
            return False
        self._height = value
        return True

    def get_age(self) -> int:
        return self._days

    def set_age(self, value: int) -> bool:
        if value < 0:
            print(f"{self.name}: Error, age can't be negative")
            return False
        self._days = value
        return True

    def show(self) -> None:
        self._stats.record_show()
        print(
            f"{self.name}: {round(self._height, 1)}cm, "
            f"{self._days} days old"
        )

    def grow(self) -> None:
        self._stats.record_grow()
        self._height += self._growth_rate

    def age(self) -> None:
        self._stats.record_age()
        self._days += 1

    def get_stats(self) -> "Plant._Stats":
        return self._stats


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        days: int,
        color: str,
        growth_rate: float = 8.0
    ) -> None:
        super().__init__(name, height, days, growth_rate)
        self.color = color
        self._blooming: bool = False

    def bloom(self) -> None:
        self._blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    class _TreeStats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shades: int = 0

        def record_shade(self) -> None:
            self._shades += 1

        def display(self) -> None:
            super().display()
            print(f"{self._shades} shade")

    def __init__(
        self,
        name: str,
        height: float,
        days: int,
        trunk_diameter: float,
        growth_rate: float = 0.0
    ) -> None:
        super().__init__(name, height, days, growth_rate)
        self.trunk_diameter = trunk_diameter
        self._stats: Tree._TreeStats = Tree._TreeStats()

    def produce_shade(self) -> None:
        self._stats.record_shade()
        print(
            f"Tree {self.name} now produces a shade of "
            f"{round(self._height, 1)}cm long and "
            f"{self.trunk_diameter}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def get_stats(self) -> "Tree._TreeStats":
        return self._stats


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        days: int,
        harvest_season: str,
        growth_rate: float = 2.1
    ) -> None:
        super().__init__(name, height, days, growth_rate)
        self.harvest_season = harvest_season
        self.nutritional_value: int = 0

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 1

    def age(self) -> None:
        super().age()
        self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        days: int,
        color: str,
        growth_rate: float = 30.0
    ) -> None:
        super().__init__(name, height, days, color, growth_rate)
        self._seeds: int = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def age(self) -> None:
        self._stats.record_age()
        self._days += 20

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


def display_plant_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.get_stats().display()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_a_year(30)}")
    print(
        f"Is 400 days more than a year? -> {Plant.is_older_than_a_year(400)}"
    )

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_plant_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_plant_stats(rose)

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_stats(oak)

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    display_plant_stats(sunflower)

    print("=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    display_plant_stats(unknown)
