#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


PLACEHOLDER = '[name]'
# get this letter content
# Reading recipient names
with open(r"Input\Names\invited_names.txt", mode="r") as names:
    invited_names = names.readlines()




with open("Input\Letters\starting_letter.txt", mode="r") as data:
    letter_content = data.read()

    for name in invited_names:
        stripped_name = name.strip()
        new_letter=letter_content.replace(PLACEHOLDER,stripped_name)

        with open(f"Output\ReadyToSend\letter_for_{stripped_name}.txt",mode="w") as sender_write:
            sender_write.writelines(new_letter)

        # print(new_letter)






    



# for name in invited_names:
#     name = f"{name.strip()},"
#     # namee = f"{name},"
#     # print(name)
#     sender_name = ' '.join(letter_content[0].split()[1:])
#     # print(sender_name)
#     # sender_name=sender_name.strip('')
#     letter_content[0]=letter_content[0].replace(sender_name,name)
#     with open(f"Output\ReadyToSend\letter_for_{name[:-1]}.txt",mode="w") as sender_write:
#         sender_write.writelines(letter_content)
    


