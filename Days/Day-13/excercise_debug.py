# Modify the code and fix the bug

# number = int(input("Which number do you want to check ? "))

# Bug here is we are taking assigment operator intead consitional argument
# if number %2 =0: it should be if number %2 ==0:

# if number %2 ==0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")


# what is type error

# When you are trying something with wrong type error


# Bug: year = input("Which year do you want to check?")
# Actually we are deviding sting with number
# To resolve this we just have converted sting into integer

# year = int(input("Which year do you want to check?"))

# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")
  

# FizzBuzz code here.. it contains errors just need to check and fix it

# Bugs:
# 1: in the else block number mentioned in the list.. just removed sequre brakets to fix
# 2: in each block of code if statement used.. just removed to fix this.used elif instead
# 3: or operator used in first condition.. where are checking 3 and 5 both condition. need to user and there.


for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)