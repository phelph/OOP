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


class Player:
    def __init__(self, name: str):
        self.name = name
        self.level = 1
        self.exp = 0
        self.max_exp = 100
        self.hp = 100
        self.max_hp = 100
        self.gold = 0
        self.max_gold = 100
        self.inventory = []
        self.equipped_item_slot = 0
        self.weapon = {"name": "Basic Sword", "Item Power": 55}

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
        dmg = self.weapon.get("Item Power", 0)
        target_hp, gained_gold = target.get_attacked(dmg)
        print(f"{self.name} attacks the {target.enemy_type} for {dmg} damage!\n")

        if target_hp <= 0:
            print(f"{self.name} killed {target.name}!\n")
            print(f"{self.name} gained {gained_gold} gold!\n")
            self.gain_exp(target.exp)
        else:
            print(f"{target.name} has {target_hp} hp left!\n")


class Warrior(Player):
    def __init__(self, name: str):
        super().__init__(name)

        self.max_hp += 20
        self.weapon = {"name": "Basic Sword", "Item Power": 55}
        self.inventory = [
            {"name": "Shield", "Item Power": 35},
            {"name": "Healing Potion", "Item Power": 10},
        ]
        if len(self.inventory) != 0:
            self.equipped_item = self.inventory[self.equipped_item_slot]

        print(
            f'You have a {self.weapon["name"]}({self.weapon["Item Power"]} Item Power) in your hand.\n'
        )

        if len(self.inventory) == 0:
            print("You don't have any items in your other hand or your backpack ye!")
        else:
            print(
                f'In your other hand you have a {self.equipped_item["name"]}({self.weapon["Item Power"]} Item Power)\n'
            )
            print("After rummaging the your backpack you also find:")
            if len(self.inventory) > 1:
                for item in self.inventory[1:]:
                    print(f'{item["name"]}, Item Power: {item["Item Power"]}')
            else:
                print("Nothing else!\n")

    def print_equipped_item(self):
        print(
            f"You currently have equipped: {self.equipped_item['name']} ({self.equipped_item['Item Power']} Item Power)"
        )

    def print_equipped_weapon(self):
        print(
            f"You currently have equipped: {self.weapon['name']} ({self.weapon['Item Power']} Item Power)"
        )
