rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line

# Importing random liberary
import random

user_input=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
names_list = [rock,paper,scissors]
if(user_input>=0 and user_input <=2):
    print(names_list[user_input])
    
    random_number = random.randint(0,2)
    print(f"Computer chose:")
    

    print(names_list[random_number])

if(user_input>=3 or user_input <0):
    print("You typed a invalid number. you lose!")
elif (user_input==0 and random_number==2):
    print("You Win")
elif ( random_number==0 and user_input==2):
    print("You lose!")
elif(random_number>user_input):
    print("You lose")
elif(user_input>random_number):
    print("You win")
elif (user_input==random_number):
    print("It's a draw")

