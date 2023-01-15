# Calculator

# Add

def add(n1,n2):
    return  n1+n2

# Subtract

def subtract(n1,n2):
    return n1-n2


# Mulitply

def mulitply(n1,n2):
    return n1*n2

# Devide

def devide(n1,n2):
    return n1/n2


operations={
    "+" :add,
    "-": subtract,
    "*":mulitply,
    "/": devide
}

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation from the line above: ")

function=operations[operation_symbol]

first_answer = function(num1,num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")

# Difference between return and print statement

operation_symbol_2 = input("Pick anotehr operation: ")

num3 = int(input("What's the third number?: "))



function = operations[operation_symbol_2]

second_answer = function(first_answer,num3)

print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")

