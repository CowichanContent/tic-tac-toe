from art import title, gameboard

title = title
gameboard = gameboard
chosen_positions = []

positions = {"ul": 16,
             "um": 21,
             "ur": 25,
             "ml": 59,
             "mm": 63,
             "mr": 68,
             "ll": 102,
             "lm": 106,
             "lr": 111,
             }


def player1_turn():
    global gameboard
    global game_on
    if game_on:
        position_choice_1 = input("Player 1, what position do you choose? (ur: upper right, mm: middle middle, "
                                  "ll: lower left, etc) ")
        if position_choice_1 not in chosen_positions:
            gameboard = gameboard[:positions.get(position_choice_1)] + "X" + gameboard[positions.get(position_choice_1) + 1:]
            chosen_positions.append(position_choice_1)
            if len(chosen_positions) == 9:
                print("Game Over- No winner")
                game_on = False
                return gameboard
            return gameboard, game_on
        else:
            print("That position was already chosen.")
            player1_turn()
    else:
        return gameboard


def player2_turn():
    global gameboard
    global game_on
    if game_on:
        position_choice_2 = input("Player 2, what position do you choose? (ur: upper right, "
                                  "mm: middle middle, ll: lower left, etc) ")
        if position_choice_2 not in chosen_positions:
            gameboard = gameboard[:positions.get(position_choice_2)] + "O" + gameboard[positions.get(position_choice_2) + 1:]
            chosen_positions.append(position_choice_2)
            if len(chosen_positions) == 9:
                print("Game Over")
                game_on = False
            return gameboard, game_on
        else:
            print("That position was already chosen.")
            player2_turn()
    else:
        return gameboard

def check_if_player1_wins():
    global gameboard
    global game_on
    if gameboard[positions["ul"]] == gameboard[positions["um"]] == gameboard[positions["ur"]] == 'X':
        print("You win!")
        game_on = False
        return game_on
    if gameboard[positions["ul"]] == gameboard[positions["ml"]] == gameboard[positions["ll"]] == 'X':
        print("You win!")
        game_on = False
        return game_on
    if gameboard[positions["ur"]] == gameboard[positions["mr"]] == gameboard[positions["lr"]] == 'X':
        print("You win!")
        game_on = False
        return game_on
    if gameboard[positions["ul"]] == gameboard[positions["mm"]] == gameboard[positions["lr"]] == 'X':
        print("You win!")
        game_on = False
        return game_on
    if gameboard[positions["ur"]] == gameboard[positions["mm"]] == gameboard[positions["ll"]] == 'X':
        print("You win!")
        game_on = False
        return game_on
    if gameboard[positions["ll"]] == gameboard[positions["lm"]] == gameboard[positions["lr"]] == 'X':
        print("You win!")
        game_on = False
        return game_on


def check_if_player2_wins():
    global gameboard
    global game_on
    if gameboard[positions["ul"]] == gameboard[positions["um"]] == gameboard[positions["ur"]] == 'O':
        print("You win!")
        game_on = False
        return game_on
    if gameboard[positions["ul"]] == gameboard[positions["ml"]] == gameboard[positions["ll"]] == 'O':
        print("You win!")
        game_on = False
        return game_on
    if gameboard[positions["ur"]] == gameboard[positions["mr"]] == gameboard[positions["lr"]] == 'O':
        print("You win!")
        game_on = False
        return game_on
    if gameboard[positions["ul"]] == gameboard[positions["mm"]] == gameboard[positions["lr"]] == 'O':
        print("You win!")
        game_on = False
        return game_on
    if gameboard[positions["ur"]] == gameboard[positions["mm"]] == gameboard[positions["ll"]] == 'O':
        print("You win!")
        game_on = False
        return game_on
    if gameboard[positions["ll"]] == gameboard[positions["lm"]] == gameboard[positions["lr"]] == 'O':
        print("You win!")
        game_on = False
        return game_on

print(title)

game_on = True
print(gameboard)
while game_on:
    print(player1_turn()[0])
    check_if_player1_wins()
    print(player2_turn()[0])
    check_if_player2_wins()






