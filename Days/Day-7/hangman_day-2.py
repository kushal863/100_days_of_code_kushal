#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
    # for each letter in the chose_word, add a "_" to representing each letter to guses
import random
choose_word = random.choice(word_list)

word_len = len(choose_word)

blanks_letter= []

for _ in range(word_len):
    blanks_letter+='_'


#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
user_input= input("Guess a Letter:").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# if the letter matches at that possition, than reveal the letter in display at that possition
# for example if the user guess is "a" and the choosen word is "saini"
    # then the display word should be ["_","a","_","_","_"]


for posstion in range(word_len):
    if choose_word[posstion] ==user_input:
        blanks_letter[posstion]=user_input
    else:
        pass
print(blanks_letter)