#Step 1 

# Step to do in the final step:
 # Update the word list to use the 'word_list' from hangman_words.py
# Delete this line ::: word_list = ["aardvark", "baboon", "camel"]

# Import words list from hangman_words.py
# importing hangman_art.py file for stages and logo
from hangman_art import logo,stages
from hangman_words import word_list
# Importing the random module to chose the word
import random
print(logo)

choose_word = random.choice(word_list)
# Coementing the testing code as i don't want to show guessed the word to the user
print(f"Choosed Word: {choose_word}")

word_len = len(choose_word)

blanks_letter= []

for _ in range(word_len):
    blanks_letter+='_'

# ToDo:1 Use a while loop to let user guess again. The loop should only stop  once the user gussed all the letters in the choosen word and display has no
# more "_". Then you can tell the user, they've won.

# Create a valriable lives to keep track number of lives left
lives = 6
End_of_game = False

while not End_of_game and lives>=0:
    user_input= input("Guess a Letter: ").lower()
    # Condition in case guess word not found in the chossen word. Dead in each wrong guessed.
    if user_input not in choose_word:
        # Tell the user that you gussed the wrong word
        print(f"You guessed {user_input}, that's not in the word. You lose a life.")
        # Adding just to enhance user experience
        print("-----------------------")
        print(stages[lives])
        lives -=1
    elif user_input in blanks_letter:
        print(f"You're already guessed {user_input}")

    
    for posstion in range(word_len):
      # condition in case guessed word is correct and filling the blanks with that work.
        if choose_word[posstion] ==user_input:
            blanks_letter[posstion]=user_input
    print(' '.join(blanks_letter))
    if '_' not in blanks_letter :
        End_of_game = True
        print("You Won!")
    elif lives<0:
      print("You Lose!")





