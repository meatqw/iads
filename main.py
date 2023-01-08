import requests
from dynamic.dynamic import create_driver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import time
import pickle


class Cookies:
    def __init__(self, file):
        self.file = file

    def save(self, cookies):
        pickle.dump(cookies, open(self.file,"wb"))

    def load(self):
        cookies = pickle.load(open("cookies.pkl", "rb"))
        return cookies


def auth():
    """Auth, save cookies"""
    driver = create_driver()
    time.sleep(2)

    driver.get('https://app.searchads.apple.com/cm/app/customreports')
    time.sleep(10)
    
    # save cookies
    Cookies('cookies').save(driver.get_cookies())

    driver.close()

auth()