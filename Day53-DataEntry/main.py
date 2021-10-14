from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import lxml
import time

FORM = "https://forms.gle/mqMLi3qUqUoCeufR6"
CHROME_DRIVER_PATH = "/Users/olivera/Documents/DevelopmentDrivers/chromedriver"

User_Agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15"
Accept_Language = "en-us"

hearders = {
    "User-Agent": User_Agent,
    "Accept-Language": Accept_Language
}

response = requests.get("https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D", headers=hearders)
site = response.text
soup = BeautifulSoup(site, 'lxml')

all_prices = soup.findAll(class_ = "list-card-price")
prices = [price.text for price in all_prices]

all_adress = soup.findAll(class_="list-card-addr")
adresses = [adress.text for adress in all_adress]

links = []
all_links = soup.select(".list-card-info a")
for link in all_links:
    if "http" not in link["href"]:
        links.append(f"https://www.zillow.con{link['href']}")
    else:
        links.append(link["href"])

driver = webdriver.Chrome(CHROME_DRIVER_PATH)

for n in range(len(all_links)):
    driver.get(FORM)
    time.sleep(2)

    type_adress = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    type_price = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    type_link = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    type_adress.send_keys(adresses[n])
    type_price.send_keys(prices[n])
    type_link.send_keys(links[n])
    submit.click()

driver.close()