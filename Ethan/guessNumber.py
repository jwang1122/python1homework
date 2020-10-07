"""
 Guess the number that computer make up.
"""
import random

random_number = random.randint(1, 100)

win = False
Turns_Player_1 = 0
while win == False:
    Your_guess = input(" Player 1: Enter a number between 1 and 100: ")
    Turns_Player_1 += 1
    if random_number == int(Your_guess):
        print("Good Job, now wait for the player 2 to go!")
        print("Number of turns you have used: ", Turns_Player_1)
        win == True
        break
    else:
        if random_number > int(Your_guess):
            print("Your Guess was low, Please enter a higher number")
        else:
            print("your guess was high, please enter a lower number")


import random

random_number = random.randint(1, 100)

win = False
Turns_Player_2 = 0
while win == False:
    Your_guess = input(" Player 2: Enter a number between 1 and 100: ")
    Turns_Player_2 += 1
    if random_number == int(Your_guess):
        print("Good Job!")
        print("Number of turns you have used: ", Turns_Player_2)
        win == True
        break
    else:
        if random_number > int(Your_guess):
            print("Your Guess was low, Please enter a higher number")
        else:
            print("your guess was high, please enter a lower number")

if Turns_Player_1 < Turns_Player_2:
    print("Congratulations, Player 1 won!")
elif Turns_Player_2 < Turns_Player_1:
    print("Congratulations, Player 2 won!")
else:
    print("Good Game, It was a tie!")
