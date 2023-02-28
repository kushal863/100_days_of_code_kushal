from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_class = Menu()

coffee_maker_class = CoffeeMaker()

money_machine_class = MoneyMachine()

# menu_item_class = MenuItem()


machine_power = True

while machine_power:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    menu_items = menu_class.get_items()

    if user_input=="off":
        machine_power=False
    elif user_input =="report":
        coffee_maker_class.report()
        money_machine_class.report()
    else:
        drink = menu_class.find_drink(user_input)
        if coffee_maker_class.is_resource_sufficient(drink) and money_machine_class.make_payment(drink.cost):                        
                        coffee_maker_class.make_coffee(drink)


    

            


# print(menu_class.get_items().split('/'))