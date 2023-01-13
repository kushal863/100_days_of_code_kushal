from replit import clear
from art import logo

print(logo)
print("Welcome to the secret auction program.")

def dict_max(dic):
    max_value = max(dic.values())
    for k,v in dic.items():
        if dic[k]==max_value:
            return [k,dic[k]]


dic ={}
any_other =True
while any_other:
            
    user_name =input ("What is your name?: ")
    bid =float(input("What's your bid?: $"))
    another_bid =input("Are there any other bidders? Type 'yes' or 'no'.\n")
    dic[user_name]=bid

    if another_bid=="yes":
        clear ()
        any_other=True
      
    elif another_bid=='no':
        max_list =dict_max(dic)
        print(f"The winner is {max_list[0]} with a bid of ${int(max_list[1])}.")
        any_other =False





