import smtplib
import datetime as dt
import random
import os
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

def send_email():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            my_email,
            "devon@beepboop.us",
            f"Subject:{random_quote}\n\n",
        )


now = dt.datetime.now()
day_of_week = now.weekday()


with open("quotes.txt", "r") as file:
    lines = [line.strip() for line in file]

random_quote = random.choice(lines)

if day_of_week == 0:
    send_email()
