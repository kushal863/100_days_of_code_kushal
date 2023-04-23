import math
import pandas as pd
import itertools
import pandas as pd
import numpy as pd
"""
1) Write a python script to determine odd  number from given a sequence of numbers?
Answer: Input => [2, 3, 4, 5] => Output => [False, True, False, True]

"""
input = [2, 3, 4, 5]
output =[]
for num in input:
    if (num%2!=0):
        output.append(True)
    else:
        output.append(False)
# print(output)


"""
2) Modify the above code such that the function can also take characters and as well as numbers.
So if a character(string)len is odd then it returns True else False
"""



input= [12, 13, "Elephant", "Horse"] 

output =[]
for num in input:
    if type(num) ==int:
        if (num%2!=0):
            output.append(True)
        else:
            output.append(False)
    elif type(num) ==str:
            if (len(num)%2!=0):
                output.append(True)
            else:
                output.append(False)
# print(output)

"""
3) Assuming a sequence of characters given like, 'aaabbbbbbaabbbbbbbcc'. You need to determine maximum frequency
for any alphabet in continuity , your answer should contain both alphabet and its frequency in a dictionary(or a tuple)
Answer: {"b": 7} or (b, 7)
Input => "aaaabxxxbbaaaaaccxxxxx" => Output => {"a":5} or (a, 5) or {"x":5} or (x, 5)

"""

input ='aaaabxxxbbaaaaaccxxxxx'

sol ={}

current_char,current_count =None,0
max_char,max_count = None,0

for i in input:

    if i == current_char:
        current_count+=1
    else:
        # Move to next charecter
        current_count =1
        current_char =i
    #
    if max_count< current_count:
        max_count=current_count
        max_char = current_char
        
    
sol[max_char]= max_count

# print(sol)

"""
4) Given a list of names in a list, sort them based on their length (ascending or descending). Don't worry
about ties for now. (ignore the case)
["amit", "gajanan", "ahmed"] => Ouput => ["amit", "ahmed", "gajanan"]
["samar", "chiku", "ravindra", "suraj" ] => Output => ["chiku", "samar", "suraj", "ravindra"] 

"""

input = ["amit", "gajanan", "ahmed","kushal" ,'sd']

print(sorted(input,key=len))

# Another Solution using bubble sort algorithm

for i in range(len(input)):
    for j in range(len(input)-i-1):
        if len(input[j]) > len(input[j+1]):
            input[j], input[j+1] = input[j+1], input[j]
    print(f"outer loop {i}:  {input}")
# print(input)
