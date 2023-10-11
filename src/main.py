import classes
from classes import Player, Enemy, PlayerCreator

if __name__ == "__main__":
    # print("Welcome to my little text based game!\n")
    # print("At first you have to create a new character!")
    player_creator = PlayerCreator()
    player_creator.create_player()

    # player_1 = Player(input("Name your Character!: "))
    # # player_1.gain_exp(90)p

    # player_1.show_exp()
    # enemy_one = Enemy("Diablo", 1)

    # print(f"An Enemy named {enemy_one.name} (Level {enemy_one.lvl}) has appeared!\n")

    # while True:
    #     choice = input("Would you like to attack? (y/n): ")

    #     if choice not in ["y", "n"]:
    #         print("Please enter either 'y' or 'n'")
    #     else:
    #         break

    # if choice == "y":
    #     player_1.attack(enemy_one)

    # elif choice == "n":
    #     print(f"{player_1.name} has cowardly run away!\n")
