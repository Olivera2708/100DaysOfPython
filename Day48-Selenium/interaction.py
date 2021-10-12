from selenium import webdriver

chrome_driver_path = "/Users/olivera/Documents/DevelopmentDrivers/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
number = driver.find_element_by_css_selector("#articlecount a")
print(number.text)