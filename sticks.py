import random

def ai_dict():
    ai_dict = {1:[1], 2:[1, 2]}
    key_start = 3
    for x in range(18):
        ai_dict.update({key_start:[1, 2, 3]})
        key_start += 1
    return ai_dict


def get_sticks(player, sticks):
    get_pick = False
    while get_pick == False:
        pick = int(input("How many sticks, {}? Pick 1-3.\n".format(player)))
        if pick > sticks:
            print("You don't have that many sticks!")
        elif pick >= 1 and pick <= 3:
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


def update_AI(dictionary, choices, won, player1):
    updated_dict = dictionary
    if won == True:
        for x in updated_dict:
            for comp_picks in choices:
                if comp_picks == x:
                    updated_dict[comp_picks].append(choices.get(comp_picks))
    elif won == False:
        for x in updated_dict:
            for comp_picks in choices:
                if comp_picks == x:
                    updated_dict[comp_picks].remove(choices.get(comp_picks))
    #print(updated_dict)
    game_loop_ai(updated_dict, player1)

def game_loop_ai(dictionary, player1):
    sticks = int(input("How many sticks? Pick between 1- 20\n"))
    comp_choices = {}
    while is_game_over(sticks) == False:
        sticks = sticks - get_sticks(player1, sticks)
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
    play_again = input("Do you want to play again? Enter yes or no.\n")
    if play_again.lower() == 'yes':
        if loser is "Skynet":
            update_AI(dictionary, comp_choices, False, player1)
        else:
            update_AI(dictionary, comp_choices, True, player1)
    else:
        print("Okay, maybe another time.")


def game_loop_2player():
    player1 = input("What is your name, player 1?\n")
    player2 = input("What is your name, player 2?\n")
    sticks = int(input("How many sticks are we playing with? Must be int between 1 - 500.\n"))
    while is_game_over(sticks) == False:
        sticks = sticks - get_sticks(player1, sticks)
        print("There are {} sticks left.".format(sticks))
        loser = who_lost(player1, sticks)
        if is_game_over(sticks) == True:
            break
        sticks = sticks - get_sticks(player2, sticks)
        print("There are {} sticks left.".format(sticks))
        loser = who_lost(player2, sticks)
    print("You lost, {}!".format(loser))


def main():
    choice = int(input("Do you want to play an AI or play with a human? Enter 1 for AI, 2 for human.\n"))
    if choice == 1:
        player1 = input("What is your name?\n")
        game_loop_ai(ai_dict(), player1)
    elif choice == 2:
        game_loop_2player()

if __name__ == '__main__':
    main()
