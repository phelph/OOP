import classes
from classes import Player, Enemy

if __name__ == "__main__":
    phelph = Player("Philip", "Rogue")
    # phelph.gain_exp(90)

    print(
        f"Player {phelph.name} has {phelph.exp} exp and needs {phelph.max_exp - phelph.exp} exp to level up"
    )

    enemy_one = Enemy("Diablo", 1)

    print(f"An Enemy named {enemy_one.name} (lvl {enemy_one.lvl}) has appeared!")
    choice = input("Would you like to attack? (y/n): ")
    if choice == "y":
        phelph.attack(enemy_one)
    elif choice == "n":
        print(f"{phelph.name} has cowardly run away!")
