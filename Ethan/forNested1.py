# for i in range(1, 9):
#     for j in range(i):
#         print(i, end=' ')
#     print()



"""
print a rightangle
1 
2 2 
3 3 3 
4 4 4 4 
"""
for i in range(1, 5):
    # add some for loop code here to print more space

    for j in range(i):
        if j==0:
            print((5-i)*" "+str(i), end=' ')
        else:
            print(i, end=' ')
    print()

"""
Homework for today
print a equaliteral triangle
    1 
   2 2 
  3 3 3 
 4 4 4 4 
"""