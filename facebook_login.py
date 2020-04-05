from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
email = input("Enter our username/ email ")
password = getpass.getpass("Enter password ")
browser = webdriver.Chrome("C:\\Users\\PSSRE\\Downloads\\chromedriver")
browser.get("https://www.facebook.com")
emailbar = browser.find_element_by_id('email')
passbar = browser.find_element_by_id('pass')
emailbar.send_keys(email)
passbar.send_keys(password)
passbar.send_keys(Keys.ENTER)




