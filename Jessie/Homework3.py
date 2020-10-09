"""
Homework for today
print a equaliteral triangle
    1 
   2 2 
  3 3 3 
 4 4 4 4 
"""
for i in range(1, 5):

    for k in range(4, i,-1):
        print(' ', end='')
    for j in range(i):
        print(i, end=' ')
    print()

"""
for fun
print a diamond
    1 
   2 2 
  3 3 3 
 4 4 4 4 
  3 3 3
   2 2
    1
"""
#top 
print("             ")
print('for fun: print a diamond')
for i in range(1, 5):
    for k in range(4, i,-1):
        print(' ', end='')
    for j in range(i):
        print(i, end=' ')
    print()
#bottem
for l in range(3,0,-1):

    for m in range(l,4):
        print(' ', end='')
    for n in range(l):
        print(l, end=' ')
    print()