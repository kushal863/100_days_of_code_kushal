# Caesar-cipher first excercise

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
        letter_index_shifted = letter_index+shift_amount
        encrpt_message+= alphabet[letter_index_shifted]
    print(f"The {direction_cipher}d text is {encrpt_message}")

caesar(message=text,shift_amount=shift,direction_cipher=direction)

