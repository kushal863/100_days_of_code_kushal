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
    resource_check =False
    data1=data[user_input]['ingredients']
    if (data1['water'] <= pending_resources['water']) & (data1['milk']<= pending_resources['milk']) & (data1['coffee']<= pending_resources['coffee']):
        global resources
        resources['water']= resources['water']-data1['water']
        resources['milk']= resources['milk']-data1['milk']
        resources['coffee']= resources['coffee']-data1['coffee']
        print(resources)
        resource_check =True
    
    return resource_check


machine_power =True     
while machine_power:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input =='report':
        print_report(resources,store_collection)
    elif (user_input=='latte') :
        ans =resource_check(MENU,resources,user_input)
        print(ans)
    elif user_input =='off':
        machine_power=False