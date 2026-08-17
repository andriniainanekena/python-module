import random

ALL_ACHIEVEMENTS: list[str] = [
    "First Steps", "Speed Runner", "Survivor", "Master Explorer",
    "Treasure Hunter", "Boss Slayer", "Crafting Genius", "World Savior",
    "Untouchable", "Unstoppable", "Strategist", "Collector Supreme",
    "Sharp Mind", "Hidden Path Finder", "Night Owl", "Dragon Slayer",
    "Pacifist", "Speedster", "Legend", "Ghost",
]

PLAYERS: list[str] = ["Alice", "Bob", "Charlie", "Dylan"]


def gen_player_achievements() -> set[str]:
    count: int = random.randint(0, len(ALL_ACHIEVEMENTS))
    picked: list[str] = random.sample(ALL_ACHIEVEMENTS, count)
    return set(picked)


def main() -> None:
    print("=== Achievement Tracker System ===")

    player_achievements: dict[str, set[str]] = {}
    for name in PLAYERS:
        player_achievements[name] = gen_player_achievements()

    for name in player_achievements:
        print(f"Player {name}: {player_achievements[name]}")

    all_distinct: set[str] = set()

    for name in player_achievements:
        all_distinct = all_distinct.union(player_achievements[name])

    print(f"All distinct achievements: {all_distinct}")

    common: set[str] = set()
    first: bool = True

    for name in player_achievements:
        if first:
            common = player_achievements[name]
            first = False
        else:
            common = common.intersection(player_achievements[name])

    print(f"Common achievements: {common}")

    for name in player_achievements:
        others: set[str] = set()

        for other_name in player_achievements:
            if other_name != name:
                others = others.union(player_achievements[other_name])

        exclusive: set[str] = player_achievements[name].difference(others)
        print(f"Only {name} has: {exclusive}")

    for name in player_achievements:
        missing: set[str] = all_distinct.difference(
            player_achievements[name]
        )
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()
