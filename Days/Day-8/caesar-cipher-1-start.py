# Caesar-cipher first excercise

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrpt, type 'decode' to decrpt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# task 1- Create a function called encrypt function that takes the text and
# shift as inputs
  # inside function , shift each letter of the text forwards in the alphabets by the shift amount
    # and print the encryped text
def encrypt(message,shift_amount):
    encrypt_message =''
    for letter in message:
        letter_index=alphabet.index(letter)
        letter_index_shifted =letter_index+shift_amount
        encrypt_message+=alphabet[letter_index_shifted]
    print(f"The encoded text is {encrypt_message}")

                


  

encrypt(text,shift)