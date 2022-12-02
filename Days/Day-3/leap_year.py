# Write a program to check wheather a given year is leap year or not

year = int(input("Which year do you want to check?"))

if year % 400 ==0 and year %100 ==0:
    print("Leap year.")
elif year%4==0 and year%100!=0:
    print("Leap year.")
else:
    print(f"Not leap year")



# Another way

if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Leap Year.")
        else:
            print("Not leap year.")    
    else:
        print("Leap year.")
        
else:
    print("Not leap year.")

