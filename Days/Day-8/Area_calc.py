#Write your code below this line 👇
import math

def paint_calc(height=2,width=4,cover=5):
    total_cans=(height*width)/coverage
    # Using  ceil to round up a number
    total_cans_round = math.ceil(total_cans)
    print(f"You'll need {total_cans_round} cans of paint.")




#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

