import datetime as dt
from smtplib import SMTP
import random
from constant import MY_EMAIL_ADDRESS,MY_PASSWORD, RECEIVER_EMAIL_ADDRESS

# Raading Data for quotes
with open('quotes.txt','r') as data_souce:
    data = data_souce.readlines()


# using random Module to choose quote randomly
quote = random.choice(data)

quote_upd = f"Hi, \n\n {quote} \n\n Thanks \n Kushal Saini"

def mail_sender_client(cls_smtp,sender_address:str,sender_password:str,receiver_address:str,msg:str):
    with cls_smtp("smtp.gmail.com") as connection:
        connection.starttls()

        connection.login(user= sender_address,password=sender_password)

        connection.sendmail(from_addr=sender_address,to_addrs=receiver_address,
                        msg=f"Subject:Motivation\n\n {msg}",
                        )


if __name__ =="__main__":
    mail_sender_client(cls_smtp=SMTP,sender_address=MY_EMAIL_ADDRESS,sender_password=MY_PASSWORD,
                       receiver_address=RECEIVER_EMAIL_ADDRESS,msg=quote_upd)