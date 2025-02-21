import os
from dotenv import load_dotenv

import boto3

load_dotenv()


class Notify:
    def __init__(self):
        self.my_number = os.getenv("MY_NUMBER")

    def send_sms(self, message):
        sns = boto3.client('sns', region_name='us-east-1')
        response = sns.publish(
        PhoneNumber=self.my_number,
        Message=f'Hello from AWS SNS!{message}'
        )