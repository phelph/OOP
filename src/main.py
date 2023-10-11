import classes
from classes import Player, Enemy, PlayerCreator

if __name__ == "__main__":
    print("Welcome to my little text based game!\n")
    print("At first you have to create a new character!")

    player_1 = PlayerCreator().create_player()

    player_1.show_exp()
    enemy_one = Enemy("Demon", player_1.level)

    print(
        f"A {enemy_one.type} (Level {enemy_one.lvl}, HP: {enemy_one.hp}) has appeared out of a dark corner!\n"
    )

    while True:
        choice = input("Would you like to attack? (y/n): ")

        if choice not in ["y", "n"]:
            print("Please enter either 'y' or 'n'")
        else:
            break

    if choice == "y":
        player_1.attack(enemy_one)

    elif choice == "n":
        print(f"{player_1.name} has cowardly run away!\n")
