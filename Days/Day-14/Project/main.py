"""
# To do list..

# Print logo in the first place
# Read dictionary data from another file
# Create a function to select random key

# selectint first random value
printing second logo in between
# selecting second random value
# create a maping with A and B( a means first random number and b means second random number)
# comparing values.. if its true then calculating score
# if its wrong then printing final score with sting

"""




# Print logo in the first place
from art import logo,vs
# Read dictionary data from another file
from game_data import data
import random

#select first random start

def generate_random_name(data):
    """
    This will generate a random number
    """
    names=[]

    for i in data:
        for k,v in i.items():
            if k=='name':
                names.append(v)
    return random.choice(names)

def folower_count(data,name):
    """
    This will return corresponding follower count
    
    """
    folower_count =0
    for i in data:
        if i['name']==name:
            folower_count=i['follower_count']

    return folower_count

# function to get two stars data using a for first and b for b

def generate_two_stars(data):
    answer =['A','B']
    final_dict={}

    for i in range(2):
        global random_name
        random_name = generate_random_name(data)
        final_dict[answer[i]]={random_name:folower_count(data,random_name)}
    return final_dict
final=generate_two_stars(data)

def compare(data,user_input):
    win=True
    final = generate_two_stars(data)
    
    if user_input =='A':
        print(f"A values {list(final['A'].values())[0]} and b values {list(final['B'].values())[0]}")
        if list(final['A'].values())[0] > list(final['B'].values())[0]:
            
            win =True
        else:
            win=False
    elif user_input=='B':
        print(f"A values {list(final['A'].values())[0]} and b values {list(final['B'].values())[0]}")
        if list(final['A'].values())[0] < list(final['B'].values())[0]:
            
            win =True
        else:
            win=False
    return win


# A_B = True
# print(logo)
name_A=[key for key in final['A']][0]
name_B=[key for key in final['B']][0]
def get_all_data_random_star(data,name):
    final_dict ={}
    for dict in data:
        for k,v in dict.items():
            if dict['name']==name:
                final_dict[k]=v
    return f"Compare A: {name}, a {final_dict['description']}, from country {final_dict['country']}"


# print(get_all_data_random_star(data,name_A))
# # print(final)

# count=0
# if count==0:
#     print()
# print(vs)

def game_high_lower(data,name_1,name_2,vs,logo):
    count =0
    print(logo)
    print(get_all_data_random_star(data,name_1))
    print(vs)
    print(get_all_data_random_star(data,name_2))
    user_input = input("Who has more followers? Type 'A' or 'B' :")
    comparison_ans =compare(data,user_input)
    while comparison_ans:
            count+=1
            print(logo)
            print(f"You're right! Current Score: {count}")
            print(get_all_data_random_star(data,name_1))
            print(vs)
            print(get_all_data_random_star(data,name_2))
            user_input = input("Who has more followers? Type 'A' or 'B' :")
    print(f"Sorry, that's wrong. Final score: {count}")

    return user_input
print(game_high_lower(data=data,name_1=name_A,name_2=name_B,vs=vs,logo=logo))

# print(get_all_data_random_star(data,name_B))
# display : Compare A: Name, a description, from country name



# while comparison_ans:
#     count+=1
#     print()
# print(count)

    

