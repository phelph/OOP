from dataclasses import dataclass, field
from random import choice


@dataclass()
class Item:
    name: str = field(init=False)
    type: str
    power: int
    weight: int
    rarity: str
    durability: str = field(
        default=100,
        init=False,
    )


@dataclass()
class Weapon(Item):
    type: str = field(default="Weapon", init=False)
    weapon_type: str

    def __post_init__(self) -> None:
        self.name = f"{self.rarity} {self.weapon_type}"

    def get_name(self) -> str:
        return self.name

    def print_info(self) -> None:
        print(
            f"This is a {self.rarity} {self.weapon_type} with item level {self.power}"
        )
