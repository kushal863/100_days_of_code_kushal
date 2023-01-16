from art import logo
import random
from replit import clear
# App logo


card_numbers = [11,2,3,4,5,6,7,8,9,10,10,10,10]

# Checking if you want to play the game of not
user_input = input(f"Do you want to play a game of Blackjack? Type 'y' or 'n': ")


print(logo)
while user_input =='y':
# Your number
    your_numbers_list =[]
    computer_numbers_list =[]

    your_numbers_list.append(random.choice(card_numbers))
    your_numbers_list.append(random.choice(card_numbers))
    your_answer = sum(your_numbers_list)


    print(f"    your cards : {your_numbers_list}, current score: {your_answer}")

    # Computer input

    computer_numbers_list.append(random.choice(card_numbers))
    computer_answer = computer_numbers_list[0]


    print(f"    Computer's first card: {computer_numbers_list[0]}")



    user_another_card = input("Type 'y' to get another card, type 'n' to pass: ")

    if user_another_card =='y':
        your_another_number =random.choice(card_numbers)
        your_answer+=your_another_number
        your_numbers_list.append(your_another_number)
        print(f"your cards : {your_numbers_list}, current score: {your_answer}")
        print(f"Computer's first card: {computer_numbers_list}, final score : {computer_answer}")
        if your_answer<=21:
            user_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_another_card=='y':
                print(f"your cards : {your_numbers_list}, current score: {your_answer}")
                print(f"Computer's final hand: {computer_numbers_list}, final score : {computer_answer}")
            else:
                pass
        else:
            print(f"your cards : {your_numbers_list}, current score: {your_answer}")
            print(f"Computer's final hand: {computer_numbers_list}, final score : {computer_answer}")
            print("You lose!")
            
            
            

    if user_another_card=='n':
        print(f"computer answer {computer_answer}")
        while computer_answer<=16:
            computer_another_number=random.choice(card_numbers)
            computer_numbers_list.append(computer_another_number)
            print(computer_numbers_list)
            computer_answer+= computer_another_number
            print(computer_answer)
        if computer_answer>16 and computer_answer<=21 :
            if computer_answer > your_answer:
                # print("first condition")
                print(f"your cards : {your_numbers_list}, current score: {your_answer}")
                print(f"Computer's final hand: {computer_numbers_list}, final score : {computer_answer}")
                print("You lose!")
            elif computer_answer == your_answer:
                # print("first condition")
                print(f"your cards : {your_numbers_list}, current score: {your_answer}")
                print(f"Computer's final hand: {computer_numbers_list}, final score : {computer_answer}")
                print("Draw!")
            else:
                # print("first condition")
                computer_another_number_once_chance=random.choice(card_numbers)
                computer_numbers_list.append(computer_another_number_once_chance)
                # print(computer_numbers_list)
                computer_answer+= computer_another_number_once_chance
                if (computer_answer > your_answer) and (computer_answer<=21):
                    print(f"your cards : {your_numbers_list}, current score: {your_answer}")
                    print(f"Computer's final hand: {computer_numbers_list}, final score : {computer_answer}")
                    print("You Lose!")
                else:
                    print(f"your cards : {your_numbers_list}, current score: {your_answer}")
                    print(f"Computer's final hand: {computer_numbers_list}, final score : {computer_answer}")
                    print("You Win!")

        elif (computer_answer>21):        
            # print("fourth condition")
            print(f"your cards : {your_numbers_list}, current score: {your_answer}")
            print(f"Computer's final hand: {computer_numbers_list}, final score : {computer_answer}")
            print("You Win!")
    user_input = input(f"Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if user_input =='y':
        clear()



