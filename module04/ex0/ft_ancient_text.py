import sys
import typing


def read_file(filename: str) -> None:
    file: typing.IO[str] | None = None
    print(f"Accessing file '{filename}'")
    try:
        file = open(filename, "r")
        content: str = file.read()
        print("---")
        print(content, end="")
        print("---")
        file.close()
        print(f"File '{filename}' closed.")
    except OSError as e:
        print(f"Error: opening file '{filename}': {e}")
        if file is not None:
            file.close()


def main() -> None:
    print("=== Cyber Archives Recovery ===")
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    read_file(sys.argv[1])


if __name__ == "__main__":
    main()
