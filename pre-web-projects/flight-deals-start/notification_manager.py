from twilio.rest import Client
import os
from dotenv import find_dotenv, load_dotenv

class NotificationManager:
    def __init__(self):
        pass
    def send_message(self,city,price):
        dotenv_file = find_dotenv()z
        load_dotenv(dotenv_file)

        account_sid = os.getenv("account_sid")
        auth_token = os.getenv("auth_token")

        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            # content_sid='HXb5b62575e6e4ff6129ad7c8efe1f983e',
            body=f"There is a new price for {city} at {price}",
            # content_variables = '{"1":"12/1","2":"3pm"}',
            to = 'whatsapp:+19723458736'
        )
        print(message.status)
    #This class is responsible for sending notifications with the deal flight details.