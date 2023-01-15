from art import logo
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


# if want to run again if you say no or we can say don't want to exit

# Can do this using recurstion... calling function itself.
def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue =True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        function=operations[operation_symbol]
        answer = int(function(num1,num2))
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        continuee = input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation, or type 'exit' to the stop the calculator: ")
        if continuee =='n':
            should_continue=False
            # calculator function called again
            # be care full while calling function itself as it will be infinite loop if there are not any cndition mentioned
            calculator()
        elif continuee =='y':
            num1 = answer
        elif continuee =='exit':
            should_continue=False

calculator()

