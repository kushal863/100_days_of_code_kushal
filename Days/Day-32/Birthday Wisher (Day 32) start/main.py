from smtplib import SMTP


## Google SMTP detail
# smtp.gmail.com

## Yahoo SMTP detail
# smtp.mail.yahoo.com

"""
Sending email steps
Sender and receiver email address
Create a object with SMTP Server
then login with the connection (required sender email address and password to login)

use sendmail method. 
    Rquired stuff:
    sender email address
    receiver address
    message


"""

MSG = '''

Hello,

This is my first email generation program.

Thanks
Kushal Kumar




'''

MY_EMAIL_ADDRESS ="testbirthday14@gmail.com"
EMAIL_PASSWORD = "ozqvxshsswhgbiqb"

RECEIVER_EMAIL_LIST = ["testbirthday144@yahoo.com"]

print(EMAIL_PASSWORD)
with SMTP("smtp.gmail.com") as connection:
    connection.starttls()

    connection.login(user=MY_EMAIL_ADDRESS ,password=EMAIL_PASSWORD)

    connection.sendmail(from_addr=MY_EMAIL_ADDRESS,to_addrs=RECEIVER_EMAIL_LIST,
                        msg=f"Subject:Conding\n\n {MSG}",
                        )




 