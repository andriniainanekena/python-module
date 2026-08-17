import random

PLAYERS_RAW: list[str] = [
    "Alice", "bob", "Charlie", "dylan", "Emma",
    "Gregory", "john", "kevin", "Liam",
]


def main() -> None:
    print("=== Game Data Alchemist ===")

    print(f"Initial list of players: {PLAYERS_RAW}")

    all_capitalized: list[str] = [
        name.capitalize() for name in PLAYERS_RAW
    ]
    print(f"New list with all names capitalized: {all_capitalized}")

    already_capitalized: list[str] = [
        name for name in PLAYERS_RAW if name == name.capitalize()
    ]
    print(f"New list of capitalized names only: {already_capitalized}")

    score_dict: dict[str, int] = {
        name: random.randint(1, 1000) for name in all_capitalized
    }
    print(f"Score dict: {score_dict}")

    avg: float = round(
        sum(score_dict[k] for k in score_dict) / len(score_dict), 2
    )
    print(f"Score average is {avg}")

    high_scores: dict[str, int] = {
        name: score_dict[name]
        for name in score_dict
        if score_dict[name] > avg
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
