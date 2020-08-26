# 2020-07-16 Python Level1 Homework

1. Use shapes.py to draw a snow couple as below

![Snow Couple](snowCouple.png)

2. Reference to guessNumber.py below, modify the code, allow two players to play, whoever find the correct number first  will win the game. (try to define function instead of duplicate code.)
```py
"""
 Guess the number that computer make up.
"""
import random

random_number = random.randint(1, 100)
win = False
Turns = 0
while win == False:
    Your_guess = input("Enter a number between 1 and 100: ")
    Turns += 1
    if random_number == int(Your_guess):
        print("You won!")
        print("Number of turns you have used: ", Turns)
        win == True
        break
    else:
        if random_number > int(Your_guess):
            print("Your Guess was low, Please enter a higher number")
        else:
            print("your guess was high, please enter a lower number")

```