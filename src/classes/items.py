from dataclasses import dataclass, field
from random import choice


@dataclass()
class Item:
    durability: int = field(
        default=100,
        init=False,
    )

    def check_rarity(self):
        # Check if the Item has a 'power' attribute.
        try:
            self.power
        except AttributeError:
            print("This item does not have a power attribute.")
            return None

        # Return the rarity of the Item.
        if self.power < 10:
            return "Common"

        elif 10 <= self.power < 20:
            return "Rare"

        elif 20 <= self.power < 30:
            return "Magic"

        else:
            return "Legendary"

    def print_name_power(self) -> None:
        print(f"This is a {self.name} with item level {self.power}!")

    def get_basic_info(self) -> tuple[str, int, int]:
        return self.name, self.power, self.durability


@dataclass()
class Weapon(Item):
    """
    Attributes that have to be given for creating a weapon:
    power : int
    weight : int
    weapon_range: str
    weapon_type: str

    automaticly generated attributes:
    durability : int

    """

    power: int
    weapon_range: str
    weapon_type: str

    name: str = field(default=None)
    weight: int = field(default=10)

    item_subclass: str = field(default="Weapon", init=False)

    def __post_init__(self) -> None:
        self.rarity = self.check_rarity()
        # Name
        if self.name is None:
            self.name = f"{self.rarity} {self.weapon_type}"

    def get_name(self) -> str:
        return self.name
