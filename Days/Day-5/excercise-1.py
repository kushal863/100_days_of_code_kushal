# calculate the avg height
# understanding the for loop in detail 
# understanding of list
# Do not use in build function like sum and len

students_height = input("Input a list of student height ").split()

for i in range(0, len(students_height)):
    students_height[i] = int(students_height[i])

print(students_height)
# Create a list variable to sum up all the numbers and count each iteration
summ=0
count=0
for height in students_height:
    summ+=height
    count+=1

result = round(summ/count)
print(result)

