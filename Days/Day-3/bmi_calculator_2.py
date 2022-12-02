height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

# Type conversions
height_flt = float(height)
weight_flt = float(weight)
# using divison and exponent operator
result = int(round((weight_flt / height_flt**2), 0))

# Interpratation of bmi value
if result < 18.5:
    print(f"Your BMI is {result}, you are underweight.")
elif result < 25:
    print(f"Your BMI is {result}, you have a normal weight.")
elif result < 30:
    print(f"Your BMI is {result}, you are slightly overweight.")
elif result < 35:
    print(f"Your BMI is {result}, you are obese.")
else:
    print(f"Your BMI is {result}, you are clinically obese.")
