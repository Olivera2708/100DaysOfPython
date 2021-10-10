import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

MY_EMAIL = ""
MY_PASSWORD = ""

URL = "https://www.amazon.com/Harry-Potter-Vault-Complete-Special/dp/1647221080/ref=sr_1_5?crid=26BHARKWIIMWJ&dchild=1&keywords=harry+potter+books+set&qid=1633888488&s=specialty-aps&sprefix=Harry+Potter+%2Cdeals-intl-ship%2C274&sr=1-5"
User_Agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15"
Accept_Language = "en-us"

hearders = {
    "User-Agent": User_Agent,
    "Accept-Language": Accept_Language
}

response = requests.get(URL,  headers=hearders)

site = BeautifulSoup(response.text, 'lxml')
pricespan = site.find("span", class_="a-size-base a-color-price a-color-price")
price = float(pricespan.getText().split("$")[1])

if price < 100:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Amazon price alert!\n\nPrice is now ${price}! Buy it on following link now: \n{URL}"
            )
