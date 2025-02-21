import os
from dotenv import load_dotenv

import boto3

load_dotenv()


class Notify:
    def __init__(self):
        self.my_number = os.getenv("MY_NUMBER")

    def send_sms(self, message):
        try:
            sns = boto3.client('sns', region_name='us-east-1')
            sns.publish(
                PhoneNumber=self.my_number,
                Message=f'{message}'
            )
        except Exception as e:
            return None