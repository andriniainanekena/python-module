import sys


def main() -> None:
    args: list[str] = sys.argv
    print("=== Command Quest ===")
    print(f"Program name: {args[0]}")

    if len(args) == 1:
        print("No arguments provided!")
    else:
        user_args: list[str] = args[1:]
        print(f"Arguments received: {len(user_args)}")

        i: int = 0
        while i < len(user_args):
            print(f"Argument {i + 1}: {user_args[i]}")
            i += 1

    print(f"Total arguments: {len(args)}")


if __name__ == "__main__":
    main()
