import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        raw: str = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts: list[str] = raw.split(",")

        try:
            x: float = float(parts[0].strip())
            y: float = float(parts[1].strip())
            z: float = float(parts[2].strip())

            try:
                parts[3]
                print("Invalid syntax")
                continue
            except IndexError:
                pass

            return (x, y, z)

        except IndexError:
            print("Invalid syntax")

        except ValueError as e:
            bad: str = ""

            try:
                float(parts[0].strip())
            except ValueError:
                bad = parts[0].strip()
            except IndexError:
                pass

            if bad == "":
                try:
                    float(parts[1].strip())
                except ValueError:
                    bad = parts[1].strip()
                except IndexError:
                    pass

            if bad == "":
                try:
                    float(parts[2].strip())
                except ValueError:
                    bad = parts[2].strip()
                except IndexError:
                    pass

            print(f"Error on parameter '{bad}': {e}")


def distance_3d(
    p1: tuple[float, float, float],
    p2: tuple[float, float, float],
) -> float:
    return math.sqrt(
        (p2[0] - p1[0]) ** 2
        + (p2[1] - p1[1]) ** 2
        + (p2[2] - p1[2]) ** 2
    )


def main() -> None:
    print("=== Game Coordinate System ===")
    origin: tuple[float, float, float] = (0.0, 0.0, 0.0)

    print("Get a first set of coordinates")
    pos1: tuple[float, float, float] = get_player_pos()

    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

    dist_to_center: float = round(distance_3d(pos1, origin), 4)
    print(f"Distance to center: {dist_to_center}")

    print("Get a second set of coordinates")
    pos2: tuple[float, float, float] = get_player_pos()

    dist: float = round(distance_3d(pos1, pos2), 4)
    print(f"Distance between the 2 sets of coordinates: {dist}")


if __name__ == "__main__":
    main()
