import random

ANSWERS = ["rock", "paper", "scissors"]
RULES = {"rock": "scissors",
         "paper": "rock",
         "scissors": "paper"}
YOUR_SCORE = 0
COMP_SCORE = 0


def comp_hand_random():
    comp_hand = random.choice(ANSWERS)
    return comp_hand


def player_hand():
    return input("Please select either rock, paper, scissors:").lower()


def game():
    global YOUR_SCORE, COMP_SCORE
    print("Let's play Paper, scissors, rock!")
    while YOUR_SCORE < 10 or COMP_SCORE < 10:
        player = player_hand()
        comp = comp_hand_random()
        print(f"You chose {player} and the computer chose {comp} ")
        if player not in ANSWERS:
            print("Invalid selection, please try again")
            continue

        if player == comp:
            print("That was a tie")
        elif RULES[player] == comp:
            print("You win")
            YOUR_SCORE += 1
        else:
            print("Computer wins")
            COMP_SCORE += 1
        print(f"Your score is {YOUR_SCORE} and the computer's score is {COMP_SCORE}")

    if YOUR_SCORE == 10:
        print("You won")
    else:
        print("You lost")


if __name__ == "__main__":
    game()
