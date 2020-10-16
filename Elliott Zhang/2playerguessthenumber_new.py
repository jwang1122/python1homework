"""
 Guess the number that computer make up.
"""
import random
import math

random_number = random.randint(1, 100)
print()
print("Game - Guess a number between 1 and 100")
print()
print("Computer generated number is",random_number)
print()

player1 = "Elliott"
player2 = "Derek"
Turns = 0
win = False

def guess(player):
    player_guess = input("%s, please enter a number between 1 and 100: " % player)
    global Turns
    Turns += 1
    if random_number > int(player_guess):
        print("%s, your guess was low, please try a higher number next time!" % player)
    elif random_number < int(player_guess):
        print("%s, your guess was high, please try a lower number next time!" % player)
    else :
        print("You won!")
        print("Number of turns you have used: ", math.ceil(Turns/2))
        global win
        win = True
    print()

while win != True:
    guess(player1)
    if win != True:
        guess(player2)
print("Game over!")
print()