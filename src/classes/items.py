class Item:
    def __init__(self, power: int, weight: int):
        self.power = power
        self.weight = weight


class Weapon(Item):
    def __init__(self, power: int, weight: int):
        super().__init__(name, power, weight)
        self.attack_power = self.power * 1.5
        self.defense = self.power * 0.2


class Defensive_Item(Item):
    def __init__(self, power: int, weight: int):
        super().__init__(name, power, weight)
        self.attack_power = self.power * 0.2
        self.defense = self.power * 1.5


class Potion(Item):
    def __init__(self, power: int, weight: int):
        super().__init__(name, power, weight)

    def get_power(self):
        return self.power


class Healing_Potion(Potion):
    def __init__(self, power: int, weight: int):
        self.color = "Red"
        super().__init__(, power, weight)


class Poison(Potion):
    def __init__(self, power: int, weight: int):
        self.color = "Green"
        super().__init__(power, weight)



