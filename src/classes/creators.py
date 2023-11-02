# general imports
from dataclasses import dataclass, field
from random import choice

# my own class imports
from items import Weapon
from player import Player


class Item_Creator:
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

    def create_weapon(self):
        """
        This function creates a random weapon
        """

        # Weapon class and type
        weapon_class = ["melee", "ranged"]
        weapon_types = {"melee": ["Sword", "Axe"], "ranged": ["Bow", "Crossbow"]}

        # random creation of an instance of a weapon
        type = choice(weapon_class)
        weapon_type = choice(weapon_types[type])
        power = choice(range(1, 30))
        weight = choice(range(1, 10))
        rarity = self.check_rarity(power)

        return Weapon(power, weight, rarity, weapon_type)


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
random_weapon.print_info()
