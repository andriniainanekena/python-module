from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        artifacts,
        key=lambda artifact: artifact.get("power", 0),
        reverse=True,
    )


def power_filter(
    mages: list[dict[str, Any]], min_power: int
) -> list[dict[str, Any]]:
    return list(
        filter(lambda mage: mage.get("power", 0) >= min_power, mages)
    )


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}
    powers = list(map(lambda mage: mage.get("power", 0), mages))
    max_power = max(mages, key=lambda mage: mage.get("power", 0))["power"]
    min_power = min(mages, key=lambda mage: mage.get("power", 0))["power"]
    avg_power = round(sum(powers) / len(powers), 2)
    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power,
    }


def main() -> None:
    artifacts: list[dict[str, Any]] = [
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
        {"name": "Crystal Orb", "power": 85, "type": "focus"},
        {"name": "Shadow Cloak", "power": 60, "type": "armor"},
    ]
    mages: list[dict[str, Any]] = [
        {"name": "Alex", "power": 70, "element": "fire"},
        {"name": "Jordan", "power": 45, "element": "water"},
        {"name": "Riley", "power": 88, "element": "shadow"},
    ]
    spells = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    first, second = sorted_artifacts[0], sorted_artifacts[1]
    print(
        f"{first['name']} ({first['power']} power) comes before "
        f"{second['name']} ({second['power']} power)"
    )

    print("\nTesting power filter...")
    strong_mages = power_filter(mages, 60)
    names = [mage["name"] for mage in strong_mages]
    print(f"Mages with power >= 60: {names}")

    print("\nTesting spell transformer...")
    print(" ".join(spell_transformer(spells)))

    print("\nTesting mage stats...")
    print(mage_stats(mages))


if __name__ == "__main__":
    main()
