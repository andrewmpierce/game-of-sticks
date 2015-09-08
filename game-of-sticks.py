
def set_up():
    player1 = input("Player 1, what's your name?\n")
    player2 = input("Player 2, what's your name?\n")
    return (player1, player2)

def game_loop(players):
    sticks = int(input("How many sticks are we playing with? Must be int.\n"))
    while sticks > 0:
        take_p1 = int(input("{}, how many sticks? Pick 1-3\n".format(players[0])))
        sticks = sticks - take_p1
        if sticks <= 0:
            print("You took the last stick! You lose, {}".format(player[0]))
            break
        print("There are {} sticks left.".format(sticks))
        take_p2 = int(input("{}, how many sticks? Pick 1-3\n".format(players[1])))
        sticks = sticks - take_p2
        if sticks <= 0:
            print("You took the last stick! You lose, {}".format(players[1]))
            break
        print("There are {} sticks left.".format(sticks))



def main():
    game_loop(set_up())

main()
