import smtplib
import datetime as dt
import random

EMAIL = "olivera.radovanovic2708@gmail.com"
PASSWORD = "olivera2002"

def get_quote():
    with open("E:/Python codes/Day32-HappyBirthdayEmail/quotes.txt") as file:
        list_quotes = [quotes for quotes in file]
    return random.choice(list_quotes)

def send_email():
    message = get_quote()

    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=EMAIL, to_addrs="olivera.radovanovic2002@gmail.com", msg=f"Subject: Monday quote\n\n{message}")
    connection.close()

now = dt.datetime.now()
if now.weekday() == 5:
    send_email()

