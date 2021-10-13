from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


CHROME_DRIVER_PATH = "/Users/olivera/Documents/DevelopmentDrivers/chromedriver"
SIMILAR_ACCOUNT = "thecubicleofficial"

USERNAME = "olivera.radovanovic2708@gmail.com"
PASSWORD = "olivera02"

URL = "https://www.instagram.com/accounts/login/"


class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)

    def login(self):
        self.driver.get(URL)
        time.sleep(2)
        username = self.driver.find_element_by_name("username")
        username.send_keys(USERNAME)
        password = self.driver.find_element_by_name("password")
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(5)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(2)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        list_follow = self.driver.find_elements_by_css_selector('li button')
        for follow in list_follow:
            try:
                follow.click()
                time.sleep(1)
            except:
                no = self.driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[3]/button[2]")
                no.click()

bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
