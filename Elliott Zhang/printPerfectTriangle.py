'''
print perfect triagle
'''

n = int(input("Please enter a number: "))

for i in range(1, n):
    for m in range(n-1-i):
        print(' ',end='')

    for j in range(i):
        print(i, end=' ')
    print()