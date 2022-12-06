# Program to calculate the maximumn number without using the in buliding function

student_height = input("Input a list of student height ").split()

for i in range(0, len(student_height)):
    student_height[i] = int(student_height[i])

print(student_height)

maxx =0
for number in student_height:
    if maxx < number:
        maxx= number
print(f"The highest score in the class is: {maxx}")
