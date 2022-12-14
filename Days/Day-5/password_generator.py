#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level
# password =''
# for letter in range(nr_letters):
#     password+=random.choice(letters)
# for symbal in range(nr_symbols):
#     password+=random.choice(symbols)
# for number in range(nr_numbers):
#     password+=random.choice(numbers)

# update_pawword=[]
# for i in range(len(password)):
#         update_pawword.append(random.sample(password,k=1))
# print(password)
# print(update_pawword)
# print(random.sample(password,k=6))


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# print(random.choice(numbers))

# Creating password list
password =[]
# Apeending random letter to the list
for letter in range(nr_letters):
    password.append(random.choice(letters))
# Appending random symbols to the list
for symbal in range(nr_symbols):
    password.append(random.choice(symbols))
# Appending random numbers to the list
for number in range(nr_numbers):
    password.append(random.choice(numbers))

# using shuffle function to change to order of the password
random.shuffle(password)
# Type conversion to string again
result=''.join(password)
print(f"Here is your password: {result}")
result_sec=""
for i in password:
    result_sec+=i
print(result_sec)


#Another_approach

random.shuffle()