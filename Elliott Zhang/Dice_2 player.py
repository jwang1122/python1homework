import random



def roll():
    min = 1
    max = 6
    print("The values are....")
    d1 = random.randint(min, max)
    d2 = random.randint(min, max)
    print(d1)
    print(d2)
    return(d1 + d2)

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("Dice Rolling Game - 2 players")
    input("Now, Player 1 is rolling, hit 'Enter' to Start!")
    p1=roll()
    input("Now, Player 2 is rolling, hit 'Enter' to Start!")
    p2=roll()

    if p1 > p2:
        print("Player 1 wins!")
    elif p1 < p2:
        print("Player 2 wins!")
    else:
        print("Tie!")
    
    roll_again = input("Roll the dices again?")    
    
print("Game over!")