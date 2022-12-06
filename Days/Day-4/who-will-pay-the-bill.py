import random
name_string =input("Give me everybody's names, seperated by a comma. ")

names = name_string.split(", ")

# using randint function from random module to calculate random number
# suppose we have three number it generate random number from 0,1,2
random_number = random.randint(0,len(names)-1)

result =names[random_number]

print(len(names))


# Output
print(f"{result} is going to buy the meal today!")