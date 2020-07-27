# Program to display calendar of the given month and year

# importing calendar module
import calendar

yy = 2020 # year
mm = 7    # month

# To take month and year input from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))

 # Multiplication table (from 1 to 10) in Python

num = 11

# To take input from the user
# num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)



# Python Program to find he factors of the number

#This function computes the factor of the argument passed
def print_factors(x):
    print("The factors of",x,"are:")
    for i in range (1,x+1):
         if x % i ==0:
               print(i)
num=49

print_factors(num)


num = 1000

# Changed num variable to string, 
# and calculated the length (number of digits)
order = len(str(num))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")





print("My name is Jason Chang")
print("age:14")
print("My favorite game is Roblox and I like to play Jailbreak and Arsenal")

# python Program to convert temperature in celsius to fahrenheit


#change the value for a different result
celsius=85

# calculate fahrenheit
fahrenheit=85
fahrenheit= (celsius*1.8)+32
print('%01f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))



