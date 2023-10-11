class PlayerCreator:
    playable_classes = ["Warrior", "Mage"]

    def create_player(self):
        player_name = input("What is your character's name?:\n")
        print("What is class do you want to play?\n")

        counter = 1
        for player_class in self.playable_classes:
            print(f"{player_class}: {counter}\n")
            counter += 1

        while True:
            try:
                player_class = int(
                    input("Please enter a number corresponding to a class\n")
                )
                if player_class in range(1, counter):
                    break
            except ValueError:
                print("THAT WASNT A NUMBER...\nPlease try again.\n")

        print(
            f"\nA {self.playable_classes[player_class - 1]} named {player_name} has woken up in a dark room and can't remember how he got there!\n"
        )


class Player:
    def __init__(self, name: str):
        while True:
            self.char_class = input(
                "What is your character's class? (Warrior/Paladin/Rogue): "
            )

            if self.char_class in ["Warrior", "Paladin", "Rogue"]:
                break
            else:
                print("Please enter either 'Warrior', 'Paladin', or 'Rogue'")

        self.name = name
        self.level = 1
        self.exp = 0
        self.max_exp = 100
        self.hp = 100
        self.max_hp = 100
        self.gold = 0
        self.max_gold = 100
        self.inventory = [{"name": "basic_sword", "dmg": 55}]
        self.equipped_item_slot = 0

    def show_exp(self):
        print(f"{self.name} has {self.exp}/{self.max_exp - self.exp} exp to level up\n")

    def gain_exp(self, exp):
        self.exp += exp
        print(f"{self.name} gained {exp} experience!\n")
        if self.exp >= self.max_exp:
            self.level_up()
            self.exp = self.exp - self.max_exp
        self.show_exp()

    def level_up(self):
        self.level += 1
        self.max_hp += 10
        self.hp = self.max_hp
        print(f"{self.name} is now level {self.level}!\n")

    def attack(self, target):
        dmg = self.inventory[self.equipped_item_slot].get("dmg", 0)
        target_hp, gained_gold = target.get_attacked(dmg)
        print(f"{self.name} attacks {target.name} for {dmg} damage!\n")

        if target_hp <= 0:
            print(f"{self.name} killed {target.name}!\n")
            print(f"{self.name} gained {gained_gold} gold!\n")
            self.gain_exp(target.exp)
        else:
            print(f"{target.name} has {target_hp} hp left!\n")


# class Warrior(Player):
