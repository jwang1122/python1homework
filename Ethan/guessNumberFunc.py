"""
 Guess the number that computer make up.
"""
import random

def play(player):
    random_number = random.randint(1, 100)
    print("the number is", random_number)
    win = False
    turns = 0
    while win == False:
        Your_guess = input("%s: Enter a number between 1 and 100: "%player)
        turns += 1
        if random_number == int(Your_guess):
            print("Number of turns you have used: ", turns)
            win == True
            break
        else:
            if random_number > int(Your_guess):
                print("Your Guess was low, Please enter a higher number")
            else:
                print("your guess was high, please enter a lower number")
    return turns

player1 = input("Enter your name please: ")
Turns_Player_1 = play(player1)
print("Good Job, now wait for the player 2 to go!")
player2 = input("Enter your name please: ")
Turns_Player_2 = play(player2)
if Turns_Player_1 < Turns_Player_2:
    print("Congratulations, %s won!"%player1)
elif Turns_Player_2 < Turns_Player_1:
    print("Congratulations, %s won!"%player2)
else:
    print("Good Game, It was a tie!")
