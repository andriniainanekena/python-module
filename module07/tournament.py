from typing import List, Tuple
from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex0.creature import Creature
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
)

Opponent = Tuple[CreatureFactory, BattleStrategy]


def battle(opponents: List[Opponent]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory_a, strat_a = opponents[i]
            factory_b, strat_b = opponents[j]

            c_a: Creature = factory_a.create_base()
            c_b: Creature = factory_b.create_base()

            print("\n* Battle *")
            print(c_a.describe())
            print(" vs.")
            print(c_b.describe())
            print(" now fight!")

            try:
                strat_a.act(c_a)
                strat_b.act(c_b)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    battle([
        (FlameFactory(), normal),
        (HealingCreatureFactory(), defensive),
    ])

    print()

    print("Tournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([
        (FlameFactory(), aggressive),
        (HealingCreatureFactory(), defensive),
    ])

    print()

    print("Tournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([
        (AquaFactory(), normal),
        (HealingCreatureFactory(), defensive),
        (TransformCreatureFactory(), aggressive),
    ])
