# Day - 1
print("Hello Kushal!")

# Excercise 1 - Printing

print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

#Excercise 2 - Fixing the code. all related to print statement.

# 1.Missing the double quotes before the word day
print("Day 1 - String Manipulation")

# 2.inner double quotes change to single one
print("String Concatenation is done with the '+' sign.")
# 3.Extra indentation removed
print('e.g. print("Hello " + "world")')
# 4.Extra ( in the print function removed.
print("New lines can be created with a backslash and n.")

# Excercise 3

# Input function
# Input function taking the information from user. By default its converting any data type into string.__doc__
# Below code-- print will print the hello and the user input
print("Hello " + input("Enter Name:"))

# Excercise 4
# Write a program that prints the number of charecter in user's name.
# putting input funtion in the len function to calculate length of the string.

print(len(input("What is your name? ")))

name = input("What is your name? ")
length = len(name)
print(length)

# Excercise - 4
# Write a program that switches the values stored in the variables a and b
# Note: any value of a and b
a = input("a: ")
b = input("b: ")
# lets learn this with example like if you have a cup of coffee and milk how you will switch.
# you would probably need third cup
temp = a
a = b
b = temp

print("a: " + a)
print("b: " + b)
