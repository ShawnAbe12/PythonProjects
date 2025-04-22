import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import find_dotenv, load_dotenv
import os

file = find_dotenv()
load_dotenv(file)
url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0",
          "Accept-Language":"en-US"}
requests = requests.get(url,headers=header)
soup = BeautifulSoup(requests.text,"html.parser")

list_words = soup.find("span", id="productTitle", class_="a-size-large product-title-word-break").getText().split()
result = ' '.join(list_words)
result = result.replace("é","e")

symbol = soup.find("span", class_="a-price-symbol").getText()
whole = soup.find("span", class_="a-price-whole").getText()
fraction = soup.find("span",class_="a-price-fraction").getText()

curr_price = float(whole) + float(fraction)/100






if curr_price < 100:
    dest_email = os.getenv("EMAIL")
    from_email = os.getenv("gmail")
    gmail_pass = os.getenv("gmail_app_pass")
    message = (f"Hello Shawn, \n\nThere is currently a low price for\n{result} for \n ${curr_price} at \n"
               f"{url}\n\n"
               f"Check it out ASAP before it rises again")

    with smtplib.SMTP("smtp.gmail.com", port=587) as gmail_connection:
        gmail_connection.starttls()
        gmail_connection.login(user=from_email, password=gmail_pass)
        gmail_connection.sendmail(from_addr=from_email, to_addrs=dest_email, msg=f"Subject:Amazon Price Deal"
                                                                                    f"\n\n{message}")
