print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

small_pizza= 15
medium_pizza =20
large_pizza =25

pepproni_small_pizza=3
pepproni_large_medium =3
extra_cheese_any_size=1
if (extra_cheese=='Y'):
    small_pizza+=1
    medium_pizza+1
    large_pizza+1


if (size=='S'):
    if (add_pepperoni=='Y'):
        total_bill=small_pizza+pepproni_small_pizza
        print(f"Your final bill is: ${total_bill}.")
    else:
        print("Your final bill is: ${small_pizza}.")

elif (size=='M'):
    if (add_pepperoni=='Y'):
        total_bill=medium_pizza+pepproni_large_medium
        print(f"Your final bill is: ${total_bill}.")
    else:
        print("Your final bill is: ${medium_pizza}.")
elif (size=='L'):
    if (add_pepperoni=='Y'):
        total_bill=large_pizza+pepproni_large_medium
        print(f"Your final bill is: ${total_bill}.")
    else:
        print("Your final bill is: ${large_pizza}.")



