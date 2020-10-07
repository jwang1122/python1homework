"""
 Guess the number that computer make up.
"""
import random

random_number = random.randint(1, 100)
win = False
Turns1 = 0
Turns2 = 0
player1 = "Elliott"
player2 = "Derek"

print("Computer generated number is",random_number)

while win == False:
    player1_guess = input("%s, please enter a number between 1 and 100: " % player1)
    Turns1 += 1
    if random_number == int(player1_guess):
        print("You won!")
        print("Number of turns you have used: ", Turns1)
        win == True
        break
    else:
        if random_number > int(player1_guess):
            print("%s, your guess was low, please try a higher number next time!" % player1)
        else:
            print("%s, your guess was high, please try a lower number next time!" % player1)
    print()

    player2_guess = input("%s, please enter a number between 1 and 100: " % player2)
    Turns2 += 1
    if random_number == int(player2_guess):
        print("You won!")
        print("Number of turns you have used: ", Turns2)
        win == True
        break
    else:
        if random_number > int(player1_guess):
            print("%s, your guess was low; please try a higher number next time!" % player2)
        else:
            print("%s, your guess was high, please try a lower number next time!" % player2)
    print()

print("Game over!")