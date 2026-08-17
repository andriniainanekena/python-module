import sys


def parse_scores(raw_args: list[str]) -> list[int]:
    scores: list[int] = []
    for arg in raw_args:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    return scores


def display_stats(scores: list[int]) -> None:
    total: int = sum(scores)
    average: float = total / len(scores)
    high: int = max(scores)
    low: int = min(scores)
    score_range: int = high - low

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {total}")
    print(f"Average score: {average}")
    print(f"High score: {high}")
    print(f"Low score: {low}")
    print(f"Score range: {score_range}")


def main() -> None:
    print("=== Player Score Analytics ===")

    raw_args: list[str] = sys.argv[1:]
    scores: list[int] = parse_scores(raw_args)

    if not scores:
        usage: str = "python3 ft_score_analytics.py <score1> <score2> ..."
        print(f"No scores provided. Usage: {usage}")
        return

    display_stats(scores)


if __name__ == "__main__":
    main()
