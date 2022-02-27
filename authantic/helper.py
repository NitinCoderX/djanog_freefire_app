from operator import setitem
import random
import os
from twilio.rest import Client
from django.conf import settings

def get_random_text():
    text = ""
    number_text = 9
    text_list = []
    choice = """qwetyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()[]{};':",.<>/?"""
    lists = list(choice)
    
    while(number_text):
        text_list.append(random.choice(lists))
        number_text -= 1


    return (text.join(text_list))
    
def get_random_slug(user):
    return (user + "__"+get_random_text())



def send_otp(reciver,otp):
    account_sid = settings.SID_TIW
    auth_token = settings.AUTH_TIW
    client = Client(account_sid, auth_token)

    message = client.messages \
                .create(
                     body=otp,
                     from_=settings.PHONE_TIW,
                     to=f"+{reciver}"
                 )

    print(message.sid)