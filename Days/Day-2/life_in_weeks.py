# Life in weeks excercise

age = input("What is your current age : ")

year_left = 90-int(age)

days = year_left*365
weeks = year_left*52
month = year_left*12
message=f"You have {days} days, {weeks} weeks, and {month} months left."
print(message)