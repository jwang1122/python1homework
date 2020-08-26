<<<<<<< HEAD
# Homework
## Boolean
- true or false
```
TERMINAL-

bool=True
type(bool)
<class 'bool'>
bool=False
type(bool)
<class 'bool'>
```
## making a class
- class can be for anything (I think)
```
class Books:
    def __init__(self, title, price):
        self.title=title
        self.price=price

    def __repr__(self):
        return self.title +' $'+ str(self.price)

book1=Books("Whatever",6.99)
print(book1)
TERMINAL-

Whatever $6.99 
```
## prime numbers
- only divisible by 1 and itself
```
def prime(Number):
    flag = True

    for i in range(2, (Number)):
        if(Number % i == 0):
            flag = False
            break

    if (flag and Number != 1):
        print(" %d is a Prime Number" %Number)
    else:
        print(" %d is not a Prime Number" %Number)

prime(13)
TERMINAL-

13 is a Prime Number
```
### certain range
```
def isPrime(x):
    flag = True

    for i in range(2, (x//2+1)):
        if(x % i == 0):
            flag = False
            break

    return flag and x != 1

if __name__ == "__main__":
    for i in range(2, 10):
        print("prime", i, isPrime(i))
TERMINAL-

prime 2 True
prime 3 True
prime 4 False
prime 5 True
prime 6 False
prime 7 True
prime 8 False
prime 9 False
```

```
from prime2 import *
x = 40
y = 50
for i in range (x,y+1):
    if (isPrime(i)):
        print(i, end=', ')
print()
TERMINAL-

41, 43, 47
```
### finding prime numbers
```
from prime2 import *

def rangePrime(x,y):
    list1 = []
    for i in range (x,y+1):
        if (isPrime(i)):
            list1.append(i)
    return list1

if __name__ == '__main__':
    n1 = 40
    n2 = 50
    l1 = rangePrime(n1,n2)
#    print(l1)
    print("The number of prime numbers between %d and %d is %d" %(n1,n2,len(l1)), end=', ')
TERMINAL-

The number of prime numbers between 40 and 50 is 3
```
## Dice rolling
### two dice
```
import random

"""
rolling two dice and display the result of the two dice
"""
def main():
    min = 1
    max = 6
    roll_again = "yes"
    while roll_again == "yes" or roll_again == "y":
        print("Rolling the dice...")
        print("The values are....")
        print(random.randint(min, max))
        print(random.randint(min, max))

        roll_again = input("Roll the dice again?")

if __name__ == '__main__':
    main()
TERMINAL-

Rolling the dice...
The values are...
ramdom value 1
random value 2
Roll the dice again?
if yes(or y,):
    repeats the code
else:
    ends
```
### possibility
```
import random
"""
1. Two six-sided dice are rolled. What is the probability 
that the numbers on the dice are different?

all set are 6*6=36, there are 6 equal, 30/36 are different. 
Answer: 30/36 = 5/6 = 0.83333333

2. Bob rolls 7 for 6-side dice.
What is the probability that the
sum of the numbers on his dice are no more than 10?

"""
min = 1
max = 6
count = 0
tests = 100
for i in range(tests):
    sum = 0
    dice1 = random.randint(min, max)
    dice2 = random.randint(min, max)
    # dice3 = random.randint(min, max)
    # dice4 = random.randint(min, max)
    # dice5 = random.randint(min, max)
    # dice6 = random.randint(min, max)
    # dice7 = random.randint(min, max)
    # sum = dice1 + dice2 + dice3 + dice4 + dice5 + dice6 + dice7
    # if (sum < 20):
    #     count += 1
    if(dice1 != dice2):
        count+=1
print(f"posibility for {tests} is {count / float(tests)}")
TERMINAL-

possibility for 100 is 0.79
```
## use for if __ name __ == "__ main __":
- prevents file from being ran when imported to another place
```
bleh
if __name=="__main__":
    print('blah')
TERMINAL-

import bleh
. . .
```
```
bleh
print('blah')
TERMINAL-

import bleh
blah
. . .
```
=======
# 2020-06-17 Homework
* Modify your plot.py file, make sin(x), cos(x) on same chart with title, x, y label and legend. Your chart may look like 
![sin(x) & cos(x)](sin-cos.png)
* Refer to you rollDice.py program, create a game with two player compete each other by rolling 3 dice, add the value up, who ever has greater number wins. You can ask player put down the bit money each time, record the money for each player. Every end of the round, ask player if they want play more, till they say no, display total money for both player.
>>>>>>> d228fdd8d19519201d9e71063dce5fa6eb83a55a
