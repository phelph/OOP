from dataclasses import dataclass, field
from random import choice
from items import Weapon
from player import Player


class Item_Creator:
    TYPES = ["melee", "ranged"]
    SUBTYPES = {"melee": ["Sword", "Axe"], "ranged": ["Bow", "Crossbow"]}

    def check_rarity(self):
        if self.power < 10:
            return "Common"

        elif 10 <= self.power < 20:
            return "Rare"

        elif 20 <= self.power < 30:
            return "Magic"

        else:
            return "Legendary"

    def create_weapon(self):
        type = choice(self.TYPES)
        subtype = choice(self.SUBTYPES[type])
        self.power = choice(range(1, 30))
        weight = choice(range(1, 10))
        rarity = self.check_rarity()
        return Weapon(subtype, self.power, weight, rarity)


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

        player_class = self.playable_classes[player_class - 1]
        print(
            f"\nYou (A {player_class} named {player_name}) have woken up in a dark room and can't remember how you got there!\n"
        )

        if player_class == "Warrior":
            return Warrior(player_name)


random_weapon = Item_Creator().create_weapon()
print(random_weapon)
