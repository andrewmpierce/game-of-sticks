def get_sticks(player):
    get_pick = False
    while get_pick == False:
        pick = int(input("How many sticks, {}?\n".format(player)))
        if pick >= 1 and pick <= 3:
            get_pick = True
        else:
            print("That's not right, between 1-3 sticks.")
    return pick


def is_game_over(sticks):
    if sticks <= 0:
        return True
    else:
        return False


def who_lost(player, sticks):
    if sticks <= 1:
        return player
    else:
        pass


def game_loop():
    player1 = input("What is your name, player 1?\n")
    player2 = input("What is your name, player 2?\n")
    sticks = int(input("How many sticks are we playing with? Must be int.\n"))
    while is_game_over(sticks) == False:
        sticks = sticks - get_sticks(player1)
        print("There are {} sticks left.".format(sticks))
        loser = who_lost(player1, sticks)
        is_game_over(sticks)
        sticks = sticks - get_sticks(player2)
        print("There are {} sticks left.".format(sticks))
        loser = who_lost(player2, sticks)
        is_game_over(sticks)
    print("You lost, {}!".format(loser))


def main():
    game_loop()

if __name__ == '__main__':
    main()
