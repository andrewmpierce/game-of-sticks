import random

def get_sticks(player):
    get_pick = False
    while get_pick == False:
        pick = int(input("How many sticks, {}?\n".format(player)))
        if pick >= 1 and pick <= 3:
            get_pick = True
        else:
            print("That's not right, pick between 1-3 sticks.")
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

def ai():
    ai_dict = {1:[1], 2:[1, 2]}
    key_start = 3
    for x in range(498):
        ai_dict.update({key_start:[1, 2, 3]})
        key_start += 1
    return ai_dict



def game_loop_ai(dictionary):
    player1 = input("What is your name?\n")
    sticks = int(input("How many sticks? Pick between 1- 500\n"))
    comp_choices = {}
    while is_game_over(sticks) == False:
        sticks = sticks - get_sticks(player1)
        print("There are {} sticks left.".format(sticks))
        loser = who_lost(player1, sticks)
        if is_game_over(sticks) == True:
            break
        comp_pick = random.choice(dictionary.get(sticks))
        comp_choices.update({sticks:comp_pick})
        sticks = sticks - comp_pick
        print("Skynet chose {}. There are {} sticks left.".format(comp_pick, sticks))
        loser = who_lost("Skynet", sticks)
        is_game_over(sticks)
    print("{} lost. Sucks to suck.".format(loser))
    play_again = input("Do you want to play again? yes or no?")
        if play_again.lower() == 'yes':
            game_loop_ai(ai())
        else:
            print("Okay, maybe another time.")


def game_loop_2player():
    player1 = input("What is your name, player 1?\n")
    player2 = input("What is your name, player 2?\n")
    sticks = int(input("How many sticks are we playing with? Must be int between 1 - 500.\n"))
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
    choice = int(input("Do you want to play an AI or play with a human? Enter 1 for AI, 2 for human.\n"))
    if choice == 1:
        game_loop_ai(ai())
    elif choice == 2:
        game_loop_2player()

if __name__ == '__main__':
    main()
