from twilio.rest import Client
import os
from data_manager import DataManager
from dotenv import find_dotenv, load_dotenv
import smtplib


class NotificationManager:
    def __init__(self):
        self.gmail = os.getenv("gmail")
        self.gmail_app_pass = os.getenv("gmail_app_pass")
        pass
    def send_message(self,city,price):
        dotenv_file = find_dotenv()
        load_dotenv(dotenv_file)

        account_sid = os.getenv("TWILIO_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")

        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            # content_sid='HXb5b62575e6e4ff6129ad7c8efe1f983e',
            body=f"There is a new price for {city} at {price}",
            # content_variables = '{"1":"12/1","2":"3pm"}',
            to = f'whatsapp:{os.getenv("MY_NUMBER")}'

        )
        print(message.status)
    #This class is responsible for sending notifications with the deal flight details.
    def send_email(self,city,price,stops):
        data_manager = DataManager()
        customer_emails = data_manager.get_customer_emails()
        for user in customer_emails:
            dest_email = user["email"]
            message = f"Hello {user['firstName']}, \nThere is currently a low price for the destination {city} at ${price} and its has {stops} stop(s).\nCheck it out!"
            with smtplib.SMTP("smtp.gmail.com", port=587) as gmail_connection:
                gmail_connection.starttls()
                gmail_connection.login(user=self.gmail, password=self.gmail_app_pass)
                gmail_connection.sendmail(from_addr=self.gmail, to_addrs=dest_email, msg=f"Subject:Flight Deals"
                                                                                    f"\n\n{message}")

