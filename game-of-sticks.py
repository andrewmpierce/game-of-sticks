def set_up_game():
    player1 = input("Player 1, what's your name?\n")
    player2 = input("Player 2, what's your name?\n")
    sticks = input("How many sticks are we playing with? Must be int.\n")
    return player1, player2, sticks

def main():
    set_up_game()
