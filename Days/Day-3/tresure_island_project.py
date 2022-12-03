# Writing a program to create game.
# Basically its for practicing if else block as well few functions of python

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure")

# Taking input from user using input function
first_step = input('You\'re at crossedroad, where do you want to go? Type "left" or "right".')

# Converting the string into lower case using lower function
first_step_lower = first_step.lower()

if (first_step_lower=='right'):
    print('You fell into a hole. Game Over.')
elif (first_step_lower=='left'):
    second_step = input('You\'ve come to lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim accross: Swim or wait: ')
    second_step_lower = second_step.lower()
    if (second_step_lower=='swim'):
        print("You ot attacked.Game Over.")
    elif(second_step_lower=='wait'):
         third_step = input("You arrive at the island unharmed. There is a house with three doors. one red, one yellow and one blue. Which color do you choose?: Which door? \n")
         third_step_lower = third_step.lower()
         if (third_step_lower=='blue') or (third_step_lower)=='red':
            print("You fell into the hole. Game Over.")
         elif (third_step_lower=='yellow'):
            print("You found the tresure.You Win!")
    

