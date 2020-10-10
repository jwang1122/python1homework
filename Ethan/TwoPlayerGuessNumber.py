"""
 Guess the number that computer make up.
"""
import random

def play(player):
    random_number = random.randint(1, 100)
    print(random_number)
    win = False
    turn = 0
    while win == False:
        Your_guess = input("%s: Enter a number between 1 and 100: " %player)
        turn += 1
        if random_number == int(Your_guess):
            print("Number of turns %s have used: %d"% (player,turn))
            win == True
            break
        else:
            if random_number > int(Your_guess):
                print("%s Guess was low, Please enter a higher number"%player)
            else:
                print("%s guess was high, please enter a lower number"%player)
    return turn

Turns_Player_1 = play("Player1")
print("Good Job, now wait for the player 2 to go!")
Turns_Player_2 = play("Player2")
if Turns_Player_1 < Turns_Player_2:
    print("Congratulations, Player 1 won!")
elif Turns_Player_2 < Turns_Player_1:
    print("Congratulations, Player 2 won!")
else:
    print("Good Game, It was a tie!")
