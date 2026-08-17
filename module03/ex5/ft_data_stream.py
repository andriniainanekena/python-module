import typing
import random

PLAYERS: list[str] = ["alice", "bob", "charlie", "dylan"]
ACTIONS: list[str] = [
    "run", "jump", "eat", "sleep", "move",
    "grab", "climb", "swim", "use", "release",
]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        name = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (name, action)


def consume_event(
    events: list[tuple[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        idx = random.randrange(len(events))
        event = events[idx]
        events.pop(idx)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")

    stream = gen_event()
    for i in range(1000):
        name, action = next(stream)
        print(f"Event {i}: Player {name} did action {action}")

    event_list: list[tuple[str, str]] = [next(stream) for _ in range(10)]
    print(f"Built list of 10 events: {event_list}")

    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()
