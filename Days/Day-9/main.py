from replit import clear
from art import logo

print(logo)
print("Welcome to the secret auction program.")

def dict_max(dic):
    # to check highest values in dictionary
    max_value = max(dic.values())
    for k,v in dic.items():
        if dic[k]==max_value:
            return [k,dic[k]]

def dix_max_app2(dic):

    highest_value = 0
    for k in dic:
        k_value = dic[k]
        if k_value>highest_value:
            highest_value=k_value
            name =k
    return [name,highest_value]


dic ={}
any_other =True
while any_other:            
    user_name =input ("What is your name?: ")
    bid =float(input("What's your bid?: $"))

    # Asking user if there is any other bid
    another_bid =input("Are there any other bidders? Type 'yes' or 'no'.\n")
    # Creating a dictionary here
    #Add name and user into dic dictionary 
    dic[user_name]=bid      
    if another_bid=='no':
        max_list =dict_max(dic)
        print(f"The winner is {max_list[0]} with a bid of ${int(max_list[1])}.")
        any_other =False
    elif another_bid =='yes':
        clear()





