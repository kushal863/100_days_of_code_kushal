#Step 1 
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']



word_list = ["aardvark", "baboon", "camel"]
import random
choose_word = random.choice(word_list)
# Testing Code
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
        print(stages[lives])
        lives -=1
    else:
      pass
    
    for posstion in range(word_len):
      # condition in case guessed word is correct and filling the blanks with that work.
        if choose_word[posstion] ==user_input:
            blanks_letter[posstion]=user_input
    print(blanks_letter)
    if '_' not in blanks_letter :
        End_of_game = True
        print("You Won!")
    elif lives<0:
      print("You Lose!")





