MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

store_collection=0

# resources['water']=resources['water']-MENU['cappuccino']['ingredients']['water']

# print(resources)



def print_report(remaining_resource,store_collection):
    print(f"Water: {remaining_resource['water']}")
    print(f"Milk: {remaining_resource['milk']}")
    print(f"Coffee: {remaining_resource['coffee']}")
    print(f"Money: ${store_collection}")

def resource_check(data,pending_resources,user_input):    
    
    global resources
    resource_check =False
    data1=data[user_input]['ingredients']
    if (user_input=='espresso'):
                                    
            if (data1['water'] >= pending_resources['water']):
                print(f"Sorry there is no enough water")
                
            if (data1['coffee']>= pending_resources['coffee']):
                print("Sorry there is no enough coffee")
            if (data1['water'] <= pending_resources['water']) & (data1['coffee']<= pending_resources['coffee']):
                resource_check=True

    elif (user_input=='latte') or (user_input=='cappuccino'):
        
        if (data1['water'] >= pending_resources['water']):
            print(f"Sorry there is no enough water")
            
        if (data1['milk']>= pending_resources['milk']):
            print(f"Sorry there is no enough milk")
            
        if (data1['coffee']>= pending_resources['coffee']):
            print("Sorry there is no enough resources")

        if (data1['water'] <= pending_resources['water']) & (data1['milk']<= pending_resources['milk']) & (data1['coffee']<= pending_resources['coffee']):
            resource_check =True
    return resource_check

def process_coins(data,user_input):

    """
    process coins takes data and user input as input
    Calculating coins and checking is received money enough to purchase a drink
    
    """
    global store_collection
    global resources
    data1 = data[user_input]['ingredients']
    cost = data[user_input]['cost']
    print("Please insert coins.")
    quaters = int(input("How many quaters? : "))
    dimes= int(input("How many dimes? : "))
    nickles = int(input("How many nickles? : "))
    pennies = int(input("How many pennies? : "))

    # calculate monetary value

    ans = 0.25*quaters+0.1*dimes+0.05*nickles+0.01*pennies

    if (ans >cost):
        # means enough amount to purchase a coffee
        change = round(ans-cost,2)
        print(f"Here is {change} in change.")
        print(f"Here is {user_input} ! enjoy!")

        if (user_input=='espresso'):
            store_collection+=cost
            resources['water']= resources['water']-data1['water']
            resources['coffee']= resources['coffee']-data1['coffee']
        elif (user_input=='latte') or (user_input=='cappuccino'):
            store_collection+=cost
            resources['water']= resources['water']-data1['water']
            resources['milk']= resources['milk']-data1['milk']
            resources['coffee']= resources['coffee']-data1['coffee']
    else:
        print("Sorry that's not enough money. Money refunded.")
        





machine_power =True     
while machine_power:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input =='report':
        print_report(resources,store_collection)
    elif (user_input=='latte') :
        ans =resource_check(MENU,resources,user_input)
        if ans:
            process_coins(MENU,user_input=user_input)
    elif user_input =='off':
        machine_power=False
    elif (user_input=='espresso'):
        ans = resource_check(MENU,resources,user_input)
        if ans:
            process_coins(MENU,user_input=user_input)

    elif (user_input=='cappuccino'):
        ans = resource_check(MENU,resources,user_input)
        if ans:
            process_coins(MENU,user_input=user_input)