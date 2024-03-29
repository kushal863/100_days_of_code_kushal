import math
import pandas as pd
import itertools
import numpy as np
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

# print(sorted(input,key=len))

# Another Solution using bubble sort algorithm

for i in range(len(input)):
    for j in range(len(input)-i-1):
        if len(input[j]) > len(input[j+1]):
            input[j], input[j+1] = input[j+1], input[j]
    
# print(input)



"""
5) Given two dictionary: d1 = {"a":  5, "b" : 6}, d2 = {"c" : 10}, merge them to create a new dictionary
Answer : Output => {"a" : 5, "b" : 6, "c": 10}
Input => d1 = {"a" : 10, "k" : 11}, d2 = {"b" : 12, "c" : 16}
Output => {"a": 10, "k" : 11, "b" : 12, "c" : 16}

"""
d1 = {"a" : 10, "k" : 11}
d2 = {"b" : 12, "c" : 16}
new_dic ={}

new_dic.update(d1)
new_dic.update(d2)
# print(new_dic)

"""
6) what are the methods present in list and tuples in python,can you write a code using list comprehension or for loop to determine which or any other method

which method are exclusively present in list but not present in tuples

"""


list_methods=dir(list)

tuple_methods = dir(tuple)

listt =[]
for m in list_methods:
    if m not in tuple_methods:
        listt.append(m)

# print(set(listt))




"""
7) Given a list of string which contains Name and age [ "AmitKumar34", "RavindraSingh45", "RashmiPrasad10" ]
Split them such that name and age should be present in a tuple
Answer: [[('AmitKumar', '34')], [('RavindraSingh', '45')], [('RashmiPrasad', '10')]]


"""

input=[ "AmitKumar34", "RavindraSingh45", "RashmiPrasad10" ]
sol = []
for i in input:
    name = i[:-2]
    age = i[-2:]
    sol.append([(name,age)])

# print(sol)



"""
8) Given a list of list: [[1, 2], [3, 4], [4, 5]], Flatten them such that the output should be
[1, 2, 3, 4, 4, 5]
Input => [[3, 10], [8, 9, 0, 1]] => Output => [3, 10, 8, 9, 0, 1]

"""

input = [[1, 2], [3, 4], [4, 5]]

output =[]

for i in input:
    for j in i:
        output.append(j)
# print(output)


"""
9) Given the list a given number, determine the factorial of a number
Input => factorial([6, 3, 2, 1, 0]) would return [720, 6, 2, 1, 1]
Note: Factorial of 1 and 0 is 1, and Factorial of 2 is 1x2 , factorial of 3 is 1x2x3, factorial of 4 is 1x2x3x4 etc

"""

def factorial(list1):
    result =[]
    fac =1
    for num in list1:
        # print(num)
        if num ==0 or num ==1:
            result.append(1)
        else:
            for i in range(2, num+1):
                fac = fac*i
            # print(f"{num}: {fac}")
            result.append(fac)
            fac=1

    return result
            
# print(factorial([6, 3, 2, 1, 0]))


""""
10) Given a side of polygon to you , how do you determine internal sum of angles of that polygon?
Write a function to do the same. Exmaple if the function takes 3 then output is 180, if it takes 4 then
output is 360 etc.

"""


def polygon_angle(num):
    return (num-2) * 180

print(polygon_angle(5))