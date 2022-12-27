# Caesar-cipher fouth excercise

# importing logo from the art file
from art import logo
#Printing logo in the start
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# print(text)

# test=''

# for letter in text:
#     if (letter not in alphabet):
#         test+=letter
#         print(letter)
#     else:
#         test+=letter
# print(test)



# Task-1 : Create a combine function to encrypt and decrypt. So at the end don't have to pass if else condition : Done
# Task 2  what if  the user enters a shift that is greather than the number of letter in the alphabet? : Done


# task 3 What happens if user enter  a number/symbol/space?
# Fix the code to keep the number/symbol/space when the text is encoded/decoded ?



# task 4- Can you figure out a way to ask the user if they want to restart the cipher program?
# Eg Type 'Yes' if you want to do it again. Otherwise type 'no'.

# if they type yes then ask them for the direction/text/shift again and call the caesar() function again

# Hint create a new function that call itself if they type yes.


def caesar(message,shift_amount,direction_cipher):

    encrpt_message =''
    if (direction_cipher=='decode'):
        shift_amount *= -1        
    for letter in message:
        if (letter in alphabet):
            letter_index = alphabet.index(letter)
            # Any number of shift amount handled..(Out of bond error)
            shift_amount=shift_amount%26
            letter_index_shifted = letter_index+shift_amount
            encrpt_message+= alphabet[letter_index_shifted]
        else:                        
            encrpt_message +=letter
            
    print(f"The {direction_cipher}d text is {encrpt_message}")



        

#  First approach: used while loop to excute cipher program again and again until user not typed no.

continue_cipher = True
while continue_cipher:
    direction = input("Type 'encode' to encrpt, type 'decode' to decrpt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(message=text,shift_amount=shift,direction_cipher=direction)    
    again= input("Type 'yes' if you want to do it again. Otherwise type 'no' \n")
    if (again=='no'):
        continue_cipher=False
        print("Goodbye!!")





# Another approach using recursion:
#calling cipher_recursion function itselt when user ask to run it again.

def cipher_recursion():
    direction = input("Type 'encode' to encrpt, type 'decode' to decrpt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(message=text,shift_amount=shift,direction_cipher=direction)    
    again= input("Type 'yes' if you want to do it again. Otherwise type 'no' \n")
    if (again=='yes'):
        cipher_recursion()
    else:
        print(f"Good bye!")

