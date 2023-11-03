from dataclasses import dataclass, field
from random import choice


@dataclass()
class Item:
    # name: str = field(default="", init=False)
    # item_subclass: str = field(default="", init=False)
    # power: int = field(default=0, init=False)
    # weight: int = field(default=0, init=False)
    # rarity: str = field(default="Common", init=False)
    durability: int = field(
        default=100,
        init=False,
    )

    @staticmethod
    def check_rarity(power):
        if power < 10:
            return "Common"

        elif 10 <= power < 20:
            return "Rare"

        elif 20 <= power < 30:
            return "Magic"

        else:
            return "Legendary"

    def print_name_power(self) -> None:
        print(f"This is a {self.name} with item level {self.power}!")

    def get_basic_info(self) -> tuple:
        return self.name, self.power, self.durability


@dataclass()
class Weapon(Item):
    WEAPON_RANGE = ["melee", "ranged"]
    WEAPON_TYPE = {"melee": ["Sword", "Axe"], "ranged": ["Bow", "Crossbow"]}

    item_subclass: str = field(default="Weapon", init=False)

    def __post_init__(self) -> None:
        # Basic Item info
        self.power = choice(range(1, 31))
        self.weight = choice(range(1, 11))
        self.rarity = self.check_rarity(self.power)

        # Weapon info
        self.range = choice(self.WEAPON_RANGE)
        self.weapon_type = choice(self.WEAPON_TYPE[self.range])

        # Name
        self.name = f"{self.rarity} {self.weapon_type}"

    def get_name(self) -> str:
        return self.name
