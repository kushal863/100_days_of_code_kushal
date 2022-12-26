# Caesar-cipher fouth excercise

# importing logo from the art file
from art import logo
#Printing logo in the start
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrpt, type 'decode' to decrpt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



# Task-1 : Create a combine function to encrypt and decrypt. So at the end don't have to pass if else condition

def caesar(message,shift_amount,direction_cipher):

    encrpt_message =''
    if (direction_cipher=='decode'):
        shift_amount *= -1        
    for letter in message:
        letter_index = alphabet.index(letter)
        if (letter not in alphabet):
            encrpt_message +=letter
        else:
            while (shift_amount>=26):
                shift_amount=shift_amount%26
            letter_index_shifted = letter_index+shift_amount
            encrpt_message+= alphabet[letter_index_shifted]
    print(f"The {direction_cipher}d text is {encrpt_message}")
        

caesar(message=text,shift_amount=shift,direction_cipher=direction)



# Task 2  what if  the user enters a shift that is greather than the number of letter in the alphabet?


# task 3 

# task 4- Can you figure out a way to ask the user if they want to restart the cipher program?
# Eg Type 'Yes' if you want to do it again. Otherwise type 'no'.

# if they type yes then ask them for the direction/text/shift again and call the caesar() function again

# Hint create a new function that call itself if they type yes.