import random
from replit import clear
from art import logo
# Step by Step approach

# Create a deal card function to return a card

def deal_card():
    """
    Returns a random card from the deck
    """
    card_numbers = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(card_numbers)
    return card



# Step 2: Deal the user and computer 2 cards each using deal_card()
def game_start():
    print(logo)
    user_cards =[]
    computer_cards =[]
    is_game_over =False


    def calculate_score(cards):
        """
            Takes some cards as input and return a sum
                """
            # Step 4
            # inside calculate_score() check for a blackjack ( a hand with only two cards : ace+10)
            # and return 0 instead of actual score. 0 will represent a blackjack in our game.

            # if 11 in cards and 10 in cards and len(cards)==2:
            #      return sum(cards)
        if sum(cards)==21 and len(cards)==2:
            return 0
            # Step 5
            # Inside calcualte_score() check for 11(ace). if score is already over 21, remove then
            # 11 and replace it with a 1. you might need to look up append() and remove()

        if 11 in cards and sum(cards)>21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)


    def compare(user_score,computer_score):
        if user_score==computer_score:
            return "Draw !"
        elif computer_score ==0:
            return "Lose, opponent has Blackjack "
        elif user_score==0:
            return "Win with a Blackjack "
        elif user_score >21:
            return "you went over. You Lose "
        elif computer_score>21:
            return "opponent went over. You win "
        elif user_score>computer_score:
            return 'You win! '

        else:
            return "You lose "


    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    while not is_game_over:


        # Step 3: Create a function called calculate_score() that takes a list of cards as input and returns the score
            # look up the sum() function to help you do this


            
        # Step 6: Call the calulate_score(). if the computer of user has a backjack(0) or if the
        # user's score is over 21, then the game ends.
        user_score=calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if user_score ==0 or computer_score ==0 or user_score> 21:
            is_game_over=True
        else:
            user_should_deal =input("Type 'y' to get another card, type 'n' to pass: ")
                # step 7:
            # is the game has not ended, ask the user id they want to draw another card. if yes,
            # then use the deal_card() function to add another to the user's list. if no then game ended.
            # Step 8:
            # The score will need to be rechecked with every new card drawn and the checks in hint 9 
            # need to be repeated until the game ends

            if user_should_deal =='y':
                print(user_cards)
                user_cards.append(deal_card())
                print(user_cards)
            else:
                is_game_over=True
        
        # Step 9: once the user is done, it's time to let the computer play.
        # computer should keep drawing cards as long as as it has a score lessa than 17

    while computer_score !=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        
    print(f"    your final hand {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score,computer_score))

while input(f"Do you want to play a game of Blackjack? Type 'y' or 'n': ")=='y':
    clear()
    game_start()