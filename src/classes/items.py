from dataclasses import dataclass, field
from random import choice


class Item:
    def __init__(self, power: int, weight: int):
        self.power = power
        self.weight = weight


@dataclass()
class Weapon:
    name: str = field(init=False)
    type: str
    power: int
    weight: int
    rarity: str
    durability: str = field(
        default=100,
        init=False,
    )

    def __post_init__(self):
        self.name = f"{self.rarity} {self.type}"
