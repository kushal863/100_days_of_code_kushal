


def mail_sender_client(cls_smtp,sender_address:str,sender_password:str,receiver_address:str,msg:str):
    with cls_smtp("smtp.gmail.com") as connection:
        connection.starttls()

        connection.login(user= sender_address,password=sender_password)

        connection.sendmail(from_addr=sender_address,to_addrs=receiver_address,
                        msg=f"Subject:Sunday Motivation\n\n {msg}",
                        )
