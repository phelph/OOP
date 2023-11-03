# general imports
from dataclasses import dataclass, field
from random import choice

# my own class imports
from items import Weapon
from player import Warrior


class Item_Creator:
    def create_weapon(self):
        """
        This function creates a random weapon
        """
        return Weapon()


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
print(random_weapon.get_basic_info())
