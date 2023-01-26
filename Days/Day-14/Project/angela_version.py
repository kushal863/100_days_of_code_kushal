from art import logo,vs
from game_data import data
import random
from replit import clear

def format_data(account):
    # format the account data into printable format

    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess,a_followers,b_followers):
    """
    Take the user guess and follower counts and returns if they got it right.

    Two step process
    """

    if a_followers> b_followers:
        return guess=='a'
    else:
        return guess=='b'





# Display art
print(logo)
score =0
game_should_continue =True
account_b = random.choice(data)

while game_should_continue:
    # Generate a random accout from the game data.
    account_a=account_b
    account_b = random.choice(data)
    while account_a==account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    # Ask users to guess.

    guess=input("Who has more followers? Type 'A' or 'B' :").lower()

    # check if user is correct
    ## get follower count if each account.
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']

    is_correct = check_answer(guess=guess,a_followers=a_follower_count,b_followers=b_follower_count)
    clear()
    print(logo)
    ## Use if statement to check if user is correct.
    if is_correct:
        score+=1
        print(f"You're rignt! Current score: {score}.")
    else:
        game_should_continue=False
        print(f"Sorry, that's wrong. Final score: {score}.")

    # give user feedback on their guess
    ### below one not handled at my code which i have written in main.py file

    # Making the account at postition at postion b become the next account at possition A.

    # Clear the screen