"""
 Guess the number that computer make up.
"""
import random
random_number = random.randint(1, 100)
print(random_number)
def play(player):
    win = False
    turn = 0
    while win == False:
        Your_guess = input(" %s: Enter a number between 1 and 100: " %player)
        turn += 1
        if random_number == int(Your_guess):
            print("Number of turns %s have used: %d" %(player, turn))
            win == True
            break
        else:
            if random_number > int(Your_guess):
                print("%s guess was low, Please enter a higher number" %player)
            else:
                print("%s guess was high, please enter a lower number" %player)
        print()
    return turn

## get the following function form internet
def get_index_positions(list_of_elems, element):
    ''' Returns the indexes of all occurrences of give element in
    the list- listOfElements '''
    index_pos_list = []
    index_pos = 0
    while True:
        try:
            # Search for item in list from indexPos to the end of list
            index_pos = list_of_elems.index(element, index_pos)
            # Add the index position in list
            index_pos_list.append(index_pos)
            index_pos += 1
        except ValueError as e:
            break
    return index_pos_list

Turns_Player_1 = play("player1")
Turns_Player_2 = play("player2")
Turns_Player_3 = play("player3")
Turns_Player_4 = play("player4")
Turns_Player_5 = play("player5")
Turns_Player_6 = play("player6")
Turns_Player_7 = play("player7")
Turns_Player_8 = play("player8")
Turns_Player_9 = play("player9")
Turns_Player_10 = play("player10")
players = ["player1","player2", "player3","player4","player5", "player6","player7","player8", \
    "player9","playler10" ]
turns_for_all_players = [Turns_Player_1, Turns_Player_2, Turns_Player_3,\
     Turns_Player_4, Turns_Player_5, Turns_Player_6\
        ,Turns_Player_7, Turns_Player_8, Turns_Player_9, Turns_Player_10]

#find min of turns_for_all_players
min__value = min(turns_for_all_players)

min__index = get_index_positions(turns_for_all_players, min__value)

#n = len(min__index)
print()
for i in min__index:
    print('The winner is: ' +player[i]+ ' and turns he/she used: '+str(i) )
    print()

print("Game Over!") 