from calendar import weekday
import datetime as dt
import pandas
import smtplib
import random
import os
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

now = dt.datetime.now()
day_of_week = now.weekday()


def get_random_file(folder_path):
    # Get absolute path to ensure it works across different systems
    absolute_path = os.path.abspath(folder_path)
    # Get list of all files in the folder
    files = os.listdir(absolute_path)
    # Randomly select one file
    random_file = random.choice(files)
    # Return full path to the file
    return os.path.join(absolute_path, random_file)


def prepare_template(to_name):
    # Remove the leading slash and use relative path
    template_path = get_random_file("letter_templates")
    with open(template_path, "r") as file:
        # Read the contents of the file into a string
        template_with_name = file.read()
        # Convert to_name to string and replace [NAME] with the actual name
        template_with_name = template_with_name.replace("[NAME]", str(to_name))
    return template_with_name


def send_email(to_name, to_email, template_with_name):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            my_email,
            to_email,
            f"Subject:HBD {to_name}\n\n{template_with_name}",
        )


df = pandas.read_csv("birthdays.csv")

birthdays_today = df[(df["month"] == now.month) & (df["day"] == now.day)]

for _, row in birthdays_today.iterrows():
    send_email(row["name"], row.email, prepare_template(row["name"]))
