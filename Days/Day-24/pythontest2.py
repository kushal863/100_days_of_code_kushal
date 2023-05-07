import math
import pandas as pd
import itertools
import numpy as np

"""
1) Given a numpy array : np.array([1, 2, 'a', 'b', np.nan, 'c', 'd', np.nan, 'e']), 
Determine how many nans are there in the array and also replace each nans with 'a'

"""
arr = np.array([1, 2, 'a', 'b', 'nan', 'c', 'd', 'nan', 'e'])

# Create a boolean mask to identify the NaN values
nan_mask = np.logical_or(arr=='nan', arr!=arr)

# Replace the NaN values with 'a'
arr[nan_mask] = 'a'

# Print the resulting array
# print(arr)

"""
2) Create a 10x5 matrix from range of 1:50, such that row wise sum should be in ascending order.
An example for 3x3 matrix: 
             [[1,2,3], => sum is 6
             [4,5,6], => sum is 15
             [7,8,9]] => sum is 24
"""
matrix = []
start = 1
for i in range(10):
    row =[]
    for col in range(5):
        row.append(start)
        start+=1
    matrix.append(row)
matrix.sort(key=lambda row : sum(row))
print(matrix)



"""
3) Run the command : pd.DataFrame({'a' : [1, 2 , 3, np.nan, 4, 6]})
Now try converting the column a to an integer, what happens? 
Are you able to convert data to integer?
Write your thoughts on the same.

"""

df = pd.DataFrame({'a' : [1, 2 , 3, np.nan, 4, 6]})
# My thoughts on it
#There are null values present,
# therefore an error is occurring while attempting to convert directly to an integer. 
# It is recommended to first fill the null values and then convert to numeric format.

df.a.fillna(0,inplace=True)
df=df.a.astype(int)
# print(df)



"""
4) Given a dataframe :
pd.DataFrame({"DateString": ["20180402,20170603,20190715", "20170806,20180801,20190806, 20190701"],
"ValueString" : ["008-090-019", "190-100-988-079"]})
Your job is to split the vlaue string with respect to dash and get the maximum of those, at whatever 
position is present fetch that from the datestring, for example for given cases.
Below are the answers:
20170603 => The maximum value is 90 present in the second string , so second date is selected
20190806 => The maximum value is at third string , so third date is selected

"""

df = pd.DataFrame({"DateString": ["20180402,20170603,20190715", "20170806,20180801,20190806, 20190701"],
"ValueString" : ["008-090-019", "190-100-988-079"]})

# print(df['ValueString'].str.split('-').max())


# df['max_value']=df['ValueString'].apply(lambda x : x.split('_').index(max(x.split('-'))))
df['max_number'] = df['ValueString'].apply(lambda x : max([int(val) for val in x.split('-')]))

df['max_number_index']=df['ValueString'].apply(lambda x : [int(val1) for val1 in x.split("-")].index(max([int(val) for val in x.split('-')])))
# print(df)

# Split 'DateString' column on ',' delimiter
df['DateString'] = df['DateString'].str.split(',')

# Extract value from 'DateString' based on 'max_number_index'
# df['MaxDate'] = df.apply(lambda row: row['DateString'][row['max_number_index'] ], axis=1)
df['DateString']=df.apply(lambda row : row['DateString'][row['max_number_index']],axis=1)

df = df[['DateString','max_number']]
# print(df)

"""
5) Write a funciton which can generate fibonacci sequence. So if your input is 3 then it should return 
2 as answer as 3rd fibonacci number is 2 . The fibonacci sequence is given below:
1 1 2 3 5 8 13 ... , so basically it starts with two 1s then next number is the sum of previous two numbers.
so 6th fibonacci number is 8 etc. 
## [1, 1, 2, 3, 5, 8, 13, 21, 34, 55] for input value of 10

"""
def fibonacci(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        fib_seq = [1, 1]
        for i in range(2, n):
            fib_seq.append(fib_seq[i-1]+ fib_seq[i-2])
        return fib_seq
print(fibonacci(10))


"""
6) write a function called float_range which can take float values as input and generate float ranges.
It is similar to range function in python which generates range of numbers, given two input numbers.
This function should take 3 parameters, start_range, stop_range and step_range . start_range is the start value of 
float number like 2.5 , 3.7 etc , stop is the stop value in floating number like 4.3, 5.7 etc.
The step is the step from which the numbers should be incremented from previous, for example:
float_range(1.2, 4.7, 1.2) => output => 1.2, 2.4, 3.6
float_range(2.5, 10, 1.5) => output => 4, 5.5, 7, 8.5 
similar to range function , the upper limit should not be included in the output.
"""

def float_range(start,end,step):
    res =[]
    if not isinstance(start,float) or not isinstance(end,float):
        return "Please enter float values"
    else:
        total_range= start+end
        steps = total_range /step
        while start < end:
            res.append(start)
            
            start+=step
        return [round(i,2) for i in res]

# print(float_range(1.2, 4.7, 1.2))



"""
7) Write a function called head , which can give head for given iterable (list, tuple or even generators)
head([1, 2, 10, 4, 5, 7, 12], 3) => output => [1, 2, 10]
head([2, 3, 4, 1, 10, 7, 8, 1], 5) => output => [2, 3, 4, 1, 10]

"""

def head(lst,num):
    lst1 = lst[:num]
    return lst1
# print(head([2, 3, 4, 1, 10, 7, 8, 1], 5))


"""
8) Create a class called "Rectangle" such that, it has length and width as input, it has two methods
area and perimeter, Create another class Square, make sure Square class should inherit from Rectangle,
and it should also able to generate perimeter and area. Make sure the your class should take only legitimate 
values of length and width. length and width can not be less than or equal to zero and also they do not
have string values. Make sure that these length and width can be accessed as read only.

"""

class Rectangle:

    def __init__(self,length,width) -> None:
        if isinstance(length, str) or isinstance(width,str):
            print("Please enter numeric values for length and width")
            self._length = None
            self._width = None
        elif (length <=0) or (width <=0):
            print("Please enter possitive number")
            self._length = None
            self._width = None
        else:
            self._length = length
            self._width = width
    
    @property

    def length(self):
        return self._length
    
    @property
    def width(self):
        return self._width

    def area(self):
        if self._length is not None and self._width is not None:
            return self._length * self._width
        return "Cannot calculate area"
    
    def perimeter(self):
        if self._length is not None and self._width is not None:
            
            return  2*(self._length* self._width)
        return "Cannot calculate perimeter"
    
class Square(Rectangle):

    def __init__(self, length, width) -> None:
        super().__init__(length, width)

  

# test1 = Square(12,'i')


# print(test1.area())
# print(test1.perimeter())
