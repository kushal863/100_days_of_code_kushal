##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas as pd
import os
import random
from smtplib import SMTP
from functions import mail_sender_client
from constant  import MY_EMAIL_ADDRESS,MY_PASSWORD,RECEIVER_EMAIL_ADDRESS



df=pd.read_csv('birthdays.csv')

# print(df)
data={key:[value.namee,value.email,value.month,value.day] for (key,value) in df.iterrows()}


# generate a today date

date =dt.datetime.now()
month_num = date.month
day = date.day

# print(type(day))

# Checking if birthday date
birthday_n = []
RECEIVER_EMAIL_ADDRESS = []
try:

    for k,value in data.items():
        if (month_num in value and day in value):
            print("Yes")
            birthday_n.append(value[0])
            RECEIVER_EMAIL_ADDRESS.append(value[1])
except Exception as e:
    print(f"No Once Birthday Today.")


random_letter=random.choice([letter for letter in os.listdir('letter_templates')])


CURRENT_WORKING_DIR = os.getcwd()
FILE_PATH = os.path.join(CURRENT_WORKING_DIR,'letter_templates',random_letter)

with open(FILE_PATH, 'r') as data_source:
    data = data_source.read()

# # data[0].split()[-1]
# print(data.split()[1])


for index in range(len(birthday_n)):
    data=data.replace(data.split()[1],birthday_n[index])
    mail_sender_client(cls_smtp=SMTP,sender_address=MY_EMAIL_ADDRESS,
                       sender_password=MY_PASSWORD,
                       receiver_address=RECEIVER_EMAIL_ADDRESS[index],msg=data)
