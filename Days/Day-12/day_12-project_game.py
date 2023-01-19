# Notes


import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
num = random.randint(1,100)

level = input("Choose a difficulty. Type 'easy' or 'hard': ")

guess_match=False

def response(num,guess_number):
    global guess_match
    guess_match =False
    if (guess_number>num):
        # print(f"Make a guess: {guess_number}")
        print("Too high.")
    elif(guess_number<num):
        # print(f"Make a guess: {guess_number}")
        print("Too low.")
    else:
        # print(f"Make a guess: {guess_number}")
        guess_match =True
        print(f"You got it! The answer was {guess_number}.")
guess_match =False
if level =='hard':
    count=5
    while count >0 and guess_match==False:
        print(f"You have {count} attempts remaining to guess the number.")
        num_guess = int(input("Make a guess: "))
        response(num,num_guess)
        
        count-=1
    if guess_match ==False:
        print("You've run out of guess, you lose")


if level =='easy':
    count=10
    while count >0 and guess_match==False:
        print(f"You have {count} attempts remaining to guess the number.")
        num_guess = int(input("Make a guess: "))
        response(num,num_guess)
        
        count-=1
    if guess_match ==False:
        print("You've run out of guess, you lose")


