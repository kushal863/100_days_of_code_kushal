# Instructions
"""
You are going to write a program that automatically prints the solution to the FizzBizz game

Your program should print each number from 1 to 1000 in turn.

When number is divible by 3 then instead of printing the number it should be print "Fizz"

When number is divible by 5 then instead of printing the number it should be print "Buzz"

And if the number is divisible by both 3 and 5 it should print "FizzBuzz"





"""

for number in range(1,101):
    if(number%3==0 and number%5==0):
        print("FizzBuzz")
    elif(number%3==0):
        print("Fizz")
    elif(number%5==0):
        print("Buzz")

    else:
        print(number)