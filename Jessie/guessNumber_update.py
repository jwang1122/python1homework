"""
 Guess the number that computer make up.
"""
import random

random_number = random.randint(1, 100)
win = False
Turns = 0
player1 = "John"
player2 = "Luke"
while win == False:
    John_guess = input("John, Enter a number between 1 and 100: ")
    Luke_guess= input("Luke, Enter a number between 1 and 100: ")
    Turns += 1
    if random_number==int(John_guess) and random_number==int(Luke_guess):
        print("The game is tie.")
        print("Number of turns that both of you have used: ", Turns)
        win=True
    elif random_number == int(John_guess):
        print("John, You won!")
        print("Number of turns that John has used: ", Turns)
        win = True
        
    elif random_number==int(Luke_guess):
        print("Luke, You won!")
        print("Number of turns that Luke has used: ", Turns)
        win=True

    else:
        if random_number > int(John_guess):
            print("John, Your Guess was below the number. Please enter a higher number")
        else:
            print("John, Your guess was higher than the number. Please enter a lower number")
        if random_number > int(Luke_guess):
            print("Luke, Your Guess was below the number. Please enter a higher number")
        else:
            print("Luke, Your guess was higher than the number. Please enter a lower number")
        
print("Game over!")