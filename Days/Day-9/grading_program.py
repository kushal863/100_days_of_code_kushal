# You have to access to a database of student_scores in the format of dictionary.
# the keys in student_scores are the names of students and the values are the exam scores.


# Write a program that converts their scores to grades. By the end the program, you should have a new dictionary
# called student_grades that should contain student_names for keys and their grades for values

# This is the scoring criteris

# Scores 91-100 Grade -"Outstanding"

# Scores 81-90 Grade - "Exceeds Exectations"
# Scores 71-80 Grade -"Acceptable"
# Score 70 or lower Grade ="Fail"


student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

student_grades ={}


#TODO-2: Write your code below to add the grades to student_grades.👇

for student in student_scores:
    if (student_scores[student]>=91):
        student_grades[student]='Outstanding'
    elif(student_scores[student]>=81):
        student_grades[student]='Exceeds Expectations'
    elif (student_scores[student]>=71):
        student_grades[student]='Acceptable'
    else:
        student_grades[student]='Fail'

# 🚨 Don't change the code below 👇
print(student_grades)