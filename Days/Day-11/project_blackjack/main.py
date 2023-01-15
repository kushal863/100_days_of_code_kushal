from art import logo
import random
# App logo


card_numbers = [11,2,3,4,5,6,7,8,9,10,10,10,10]

# Checking if you want to play the game of not

user_input = input(f"Do you want to play a game of Blackjack? Type 'y' or 'n': ")
print(logo)

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
    if your_answer<=21:
        user_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
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
    if computer_answer > 16 and computer_answer <=21:
        computer_another_number_once_chance=random.choice(card_numbers)
        computer_numbers_list.append(computer_another_number_once_chance)
        print(computer_numbers_list)
        computer_answer+= computer_another_number_once_chance
        print(computer_answer)
        #print(f"Computer's final hand: {computer_numbers_list}, final score : {computer_answer}")
    if (computer_answer > your_answer) and (computer_answer<=21):

        print("elif block")
        print(f"your cards : {your_numbers_list}, current score: {your_answer}")
        print(f"Computer's final hand: {computer_numbers_list}, final score : {computer_answer}")
        print("You lose!")
    if (computer_answer>21):        
        print("else block")
        print(f"your cards : {your_numbers_list}, current score: {your_answer}")
        print(f"Computer's final hand: {computer_numbers_list}, final score : {computer_answer}")
        print("You Win!")




#     another_card_number = random.choice(card_numbers)
#     another_card_answer=your_answer+ another_card_number

#     print(f"Your cards : [{num1}, {num2}, {another_card_number}], current score: {another_card_answer}")
#     print(f"Computer's first card: {num3_c}")

#     if another_card_answer >=21:


