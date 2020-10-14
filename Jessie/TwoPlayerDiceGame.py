import random

"""
rolling two dice and display the result of the two dice
"""


def main():
    min = 1
    max = 6
    roll_again = "yes"
    total_dice=0
    while roll_again == "yes" or roll_again == "y":
        print("Rolling the dices now...")
        first_dice = random.randint(min, max)
        second_dice = random.randint(min, max)
        print("The first dice is %d"%first_dice)
        print("The second dice is %d"%second_dice)
        total_dice = first_dice + second_dice + total_dice
        roll_again = input("Play again?")
    return total_dice
#if __name__ == '__main__':
#    main()

player1 = input("Player1, please enter your name: ")
player2 = input("Player2, please enter your name: ")
print("%s, it's your turn " %player1)
p1_results = main()
print("%s, your total sum is %d: " %(player1, p1_results))
print()
print("%s, it's your turn " %player2)
p2_results = main()
print("%s, your total sum is %d: " %(player2, p2_results))
print()

if p1_results > p2_results:
    print("%s wins!" %player1)
elif p1_results < p2_results:
    print("%s wins!" %player2)
else:
    print("It's a tie!")

print("Game over!")