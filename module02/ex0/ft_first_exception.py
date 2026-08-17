#!/usr/bin/env python3

def input_temperature(temp_str: str | None) -> int:
    if temp_str is None:
        raise ValueError("temperature cannot be None")
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")

    for temp_str in ("25", "abc"):
        print(f"\nInput data is '{temp_str}'")
        try:
            temp = input_temperature(temp_str)
            print(f"Temperature is now {temp}°C")
        except (ValueError, TypeError) as e:
            print(f"Caught input_temperature error: {e}")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
