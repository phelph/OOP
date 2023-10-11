class Player:
    def __init__(self, name, char_class):
        self.name = name
        self.char_class = char_class
        self.level = 1
        self.exp = 0
        self.max_exp = 100
        self.hp = 100
        self.max_hp = 100
        self.gold = 0
        self.max_gold = 100
        self.inventory = [{"name": "basic_sword", "dmg": 53}]
        self.equipped_item_slot = 0

    def level_up(self):
        self.level += 1
        self.max_hp += 10
        self.hp = self.max_hp
        print(f"{self.name} is now level {self.level}!")

    def gain_exp(self, exp):
        self.exp += exp
        print(f"{self.name} gained {exp} experience!")
        if self.exp >= self.max_exp:
            self.level_up()
            self.exp = self.exp - self.max_exp

    def attack(self, target):
        dmg = self.inventory[self.equipped_item_slot].get("dmg", 0)
        target_hp, gained_gold = target.get_attacked(dmg)
        print(f"{self.name} attacks {target.name} for {dmg} damage!")

        if target_hp <= 0:
            print(f"{self.name} killed {target.name}!")
            print(f"{self.name} gained {gained_gold} gold!")
            self.gain_exp(target.exp)
