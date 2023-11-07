import classes

if __name__ == "__main__":
    print("Welcome to my little text based game!\n")
    print("At first you have to create a new character!")

    player_1 = classes.PlayerCreator().create_player()

    player_1.show_exp()

    # player_1.take_dmg(100)
    # player_1.take_dmg(30)
