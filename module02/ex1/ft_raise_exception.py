#!/usr/bin/env python3

def input_temperature(temp_str: str | None) -> int:
    if temp_str is None:
        raise ValueError("None is not a valid temperature")
    temp_int = int(temp_str)
    if temp_int < 0:
        raise ValueError(f"{temp_int}°C is too cold for plants (min 0°C)")
    if temp_int > 40:
        raise ValueError(f"{temp_int}°C is too hot for plants (max 40°C)")
    return temp_int


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    print()
    test_values = ["25", "abc", "100", "-50"]
    for value in test_values:
        try:
            print(f"Input data is '{value}'")
            print(f"Temperature is now {input_temperature(value)}°C")
            print()
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
            print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
