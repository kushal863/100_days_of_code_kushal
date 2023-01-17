import random
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

user_cards =[]
computer_cards =[]


for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


# Step 3: Create a function called calculate_score() that takes a list of cards as input and returns the score
    # look up the sum() function to help you do this

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

    return sum(cards)