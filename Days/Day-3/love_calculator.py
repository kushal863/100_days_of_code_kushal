# Program for love calculator


print("Welcome to the Love Calculator!")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

combined_name = name1+name2
name1 = name1.lower()
name2 = name2.lower()

true_count=combined_name.count('t')+combined_name.count('r') + combined_name.count('u') + combined_name.count('e')
love_count = combined_name.count('l')+ combined_name.count('o') + combined_name.count('v') + combined_name.count('e')
#calculate true and love in both names than adding true in first place and love in second place that concat
score=int(str(true_count)+ str(love_count))
if (score<10) or (score>90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif(score>40) and (score<50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")

