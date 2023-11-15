import classes

if __name__ == "__main__":
    print("Welcome to my little text based game!\n")
    print("At first you have to create a new character!")
    creator = classes.PlayerCreator()
    player_1 = creator.create_player()

    player_1.stats.print_stats()
    player_1.equipped_weapon.print_name_power()

    # player_1.take_dmg(100)
    # player_1.take_dmg(30)
