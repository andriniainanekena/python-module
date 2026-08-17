import sys
import typing


def read_file(filename: str) -> str | None:
    print(f"Accessing file '{filename}'")
    file: typing.IO[str] | None = None
    try:
        file = open(filename)
        content: str = file.read()
        print("---")
        print(content, end="")
        print("---")
        file.close()
        print(f"File '{filename}' closed.")
        return content
    except OSError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
        sys.stderr.flush()
        if file is not None:
            file.close()
        return None


def transform(content: str) -> str:
    lines: list[str] = content.splitlines()
    return "\n".join(line + "#" for line in lines) + "\n"


def save_file(filename: str, content: str) -> None:
    print(f"Saving data to '{filename}'")
    file: typing.IO[str] | None = None
    try:
        file = open(filename, "w")
        file.write(content)
        file.close()
        print(f"Data saved in file '{filename}'.")
    except OSError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
        sys.stderr.flush()
        if file is not None:
            file.close()
        print("Data not saved.")


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    content: str | None = read_file(sys.argv[1])
    if content is None:
        return
    new_content: str = transform(content)
    print("\nTransform data:")
    print("---")
    print(new_content, end="")
    print("---")
    sys.stdout.write("\nEnter new file name (or empty): ")
    sys.stdout.flush()
    new_filename: str = sys.stdin.readline().rstrip("\n")
    if not new_filename:
        print("Not saving data.")
        return
    save_file(new_filename, new_content)


if __name__ == "__main__":
    main()
