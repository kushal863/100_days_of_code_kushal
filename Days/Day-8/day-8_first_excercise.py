# Review

def greet():
    print("First Statement")
    print("Second Statement")
    print("Third Statement")

# greet()


# Functions with input


def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

# greet_with_name('kushal')


# Funcs with more than one parameters

# Possitional Argument
# Be sure you check with possition while inputing the data

def greet_me(name,location) ->str:
    print(f"Hello {name}")
    print(f"Location of {name} is {location}")

# greet_me('kushal','Punjab')


# greet_me('Ricky','Noida')


#KEYWORD ARGUEMENT

#def my_function(a=1,b=4,c=5):
    # Do this with a
    # Then do this with b
    # Then do this with c

def greet_me(name="Kushal",location="Noida"):
    print(f"Hello {name}")
    print(f"Location of {name} is {location}")  

greet_me(location="Noida",name="Kushal")