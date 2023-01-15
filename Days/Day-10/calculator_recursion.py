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
    num1 = int(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue =True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = int(input("What's the next number?: "))
        function=operations[operation_symbol]
        answer = function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        should_continue = input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation.: ")
        if should_continue =='n':
            should_continue=False
            # calculator function called again
            # be care full while calling function itself as it will be infinite loop if there are not any cndition mentioned
            calculator()
        elif should_continue =='y':
            num1 = answer

# calculator()




# Example:

def greet():
    print("Hello Kushal")
    greet()

# Error Code = RecursionError: maximum recursion depth exceeded while calling a Python object
# greet()