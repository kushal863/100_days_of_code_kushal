print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))
tip_perc = int(input("What percentage tip would you life to give? 10, 12, or 15? "))
people = int(input("How many person to split the bill?"))

tip_amount = total_bill* (tip_perc/100)
total_bill = total_bill+ tip_amount
each_person_bill = total_bill/people
each_person_bill_round = "{:.2f}".format(each_person_bill)
print(f"Each person should pay: ${each_person_bill_round}")