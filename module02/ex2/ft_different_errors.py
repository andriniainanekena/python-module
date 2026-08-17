#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    print(f"Testing operation {operation_number}...")
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        42 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "forty-two" + 42


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for i in [0, 1, 2, 3, 4]:
        try:
            garden_operations(i)
        except ValueError as e:
            print(f"Caught {e.__class__.__name__}: {e}")
        except ZeroDivisionError as e:
            print(f"Caught {e.__class__.__name__}: {e}")
        except FileNotFoundError as e:
            print(f"Caught {e.__class__.__name__}: {e}")
        except TypeError as e:
            print(f"Caught {e.__class__.__name__}: {e}")
        else:
            if i >= 4:
                print("Operation completed successfully")

    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
