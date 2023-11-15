# general imports
from random import choice

# my own class imports
from classes.items import Weapon
from classes.player import Player, Warrior, Mage


class Item_Creator:
    def random_weapon_drop(self, player: Player):
        """
        Creates a random weapon based on the provided Player's level.

        The weapon's power level is determined by the player's level,
        ensuring that the weapon is appropriate for the player's current progression.


        Parameters:
        - player (Player): An instance of the Player class or its subclasses.
                           The player's level is used to influence the weapon's attribute and type.

        Returns:
        - Weapon: An instance of the Weapon class with attributes scaled to the player's level.

        Note:
        - The method currently assumes that the Player class has an attribute 'level'.
          If the 'level' attribute does not exist, the method will raise an AttributeError.
        """
        try:
            level = player.level

        except AttributeError:
            raise AttributeError("The Player class does not have a 'level' attribute.")

        # set a semi random power level to scale the weapon's attributes to the player's level
        power = level + choice(range(-3, 5))
        weight = choice(range(1, 11))

        # select which type of weapon to create based on what the player can use
        weapon_range = choice(player.usable_weapon_ranges)
        weapon_type = choice(player.usable_weapon_types.get(weapon_range))

        # create the weapon and return it
        return Weapon(
            power=power,
            weight=weight,
            weapon_range=weapon_range,
            weapon_type=weapon_type,
        )


class PlayerCreator:
    PLAYABLE_CLASSES = ["Warrior", "Mage"]

    def create_player(self):
        player_name = input("What is your character's name?:\n")
        print("What is class do you want to play?\n")

        counter = 1
        for player_class in self.PLAYABLE_CLASSES:
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

        player_class = self.PLAYABLE_CLASSES[player_class - 1]
        print(f"\nCharacter successfully created")

        if player_class == "Warrior":
            return Warrior(player_name)

        elif player_class == "Mage":
            return Mage(player_name)
