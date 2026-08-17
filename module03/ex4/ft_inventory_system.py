import sys


def parse_inventory(raw_args: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}

    for arg in raw_args:
        parts: list[str] = arg.split(":")

        if len(parts) != 2 or not parts[0] or not parts[1]:
            print(f"Error - invalid parameter '{arg}'")
            continue

        name: str = parts[0]
        qty_str: str = parts[1]

        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue

        try:
            qty: int = int(qty_str)

            if qty <= 0:
                print(
                    f"Quantity error for '{name}': "
                    "quantity cannot be negative/null"
                )
                continue

            inventory[name] = qty

        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")

    return inventory


def display_inventory(inventory: dict[str, int]) -> None:
    print(f"Got inventory: {inventory}")


def display_stats(inventory: dict[str, int]) -> None:
    items: list[str] = list(inventory.keys())
    total: int = sum(inventory.values())

    print(f"Item list: {items}")
    print(f"Total quantity of the {len(items)} items: {total}")

    for name in inventory.keys():
        qty: int = inventory[name]
        pct: float = round(qty / total * 100, 1)
        print(f"Item {name} represents {pct}%")

    most: str = items[0]
    least: str = items[0]

    for item in items:
        if inventory[item] > inventory[most]:
            most = item

        if inventory[item] < inventory[least]:
            least = item

    print(f"Item most abundant: {most} with quantity {inventory[most]}")
    print(
        f"Item least abundant: {least} with quantity "
        f"{inventory[least]}"
    )


def main() -> None:
    print("=== Inventory System Analysis ===")

    raw_args: list[str] = sys.argv[1:]
    inventory: dict[str, int] = parse_inventory(raw_args)

    if not inventory:
        print("No valid items provided.")
        return

    display_inventory(inventory)
    display_stats(inventory)

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
