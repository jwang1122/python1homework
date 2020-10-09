"""
 Guess the number that computer make up.
"""
import random

def play(player1, player2):
    random_number = random.randint(1, 100)
    print("the number is", random_number)
    win = False
    turns = 0
    turns_1 = 0
    turns_2 = 0
    while win == False:
        if turns%2 == 0:
            Your_guess = input("%s, it is your turn. Enter a number between 1 and 100: "%player1)
            player = player1
            turns_1 += 1
        else:
            Your_guess = input("%s, it is your turn. Enter a number between 1 and 100: "%player2)
            player = player2
            turns_2 += 1
        turns += 1
        if random_number == int(Your_guess):
            if turns%2 ==0:
                winner_turn = turns_1
            else:
                winner_turn = turns_2
            print(player + ", Congrats!! You win! The number of turns you have used: ", winner_turn)
            win == True
            break
        else:
            if random_number > int(Your_guess):
                print(player + ", your Guess was low, Please enter a higher number next time")
            else:
                print(player + ", your guess was high, please enter a lower number next time")
    return turns

player1 = input("Player #1, please enter your name please: ")
player2 = input("Player #2, Please enter your name please: ")

Turns_Player_1 = play(player1, player2)
# print("Good Job, now wait for the player 2 to go!")
# player2 = input("Enter your name please: ")
# Turns_Player_2 = play(player2)
# if Turns_Player_1 < Turns_Player_2:
#     print("Congratulations, %s won!"%player1)
# elif Turns_Player_2 < Turns_Player_1:
#     print("Congratulations, %s won!"%player2)
# else:
#     print("Good Game, It was a tie!")
