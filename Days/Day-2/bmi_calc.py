# Excercise - 2 BMI calculator
# Taking user inputs
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# Type conversions
height_flt = float(height)
weight_flt = float(weight)
# using divison and exponent operator
result = weight_flt/ height_flt**2
print(result)