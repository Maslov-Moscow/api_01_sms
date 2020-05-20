import time, os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()
vk_token = os.getenv('vk_token')
auth_token = os.getenv('auth_token')
account_sid = os.getenv('account_sid')
NUMBER_FROM = os.getenv('NUMBER_FROM')
NUMBER_TO = os.getenv('NUMBER_TO')


def get_status(user_id):
    params = {
        "access_token": vk_token,
        "user_ids": user_id,
        "fields": 'online',
        'v': 5.103
    }
    response = requests.post('https://api.vk.com/method/users.get', params)
    return response.json()["response"][0]["online"]


def sms_sender(sms_text):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=sms_text,
        from_=NUMBER_FROM,
        to=NUMBER_TO
    )

    return message.sid


if __name__ == "__main__":
    vk_id = input("Введите id ")
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
