#Step 1 

word_list = ["aardvark", "baboon", "camel"]
import random
choose_word = random.choice(word_list)

word_len = len(choose_word)

blanks_letter= []

for _ in range(word_len):
    blanks_letter+='_'

# ToDo:1 Use a while loop to let user guess again. The loop should only stop  once the user gussed all the letters in the choosen word and display has no
# more "_". Then you can tell the user, they've won.

while '_' in blanks_letter:
    user_input= input("Guess a Letter:").lower()
    for posstion in range(word_len):
        if choose_word[posstion] ==user_input:
            blanks_letter[posstion]=user_input
    print(blanks_letter)
print("You Won!")




