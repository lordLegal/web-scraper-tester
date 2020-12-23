import msvcrt as m
import pickle
import smtplib
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

print("wähle die arte von dem scraper aus click, get, write, screenshot, load_cookies")
art = str(input())
if art == "click":
    print("Bitte schrieb hier die url rein")
    url = str(input())
    print("Schreib hier den XPATH")
    xpath = str(input())
    browser = webdriver.Firefox()
    browser.get(url)
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        browser.add_cookie(cookie)
    browser.find_element_by_xpath(xpath).click()
    browser.quit()
else:
    pass
if art == "get":
    print("Bitte schrieb hier die url rein")
    url = str(input())
    print("Schreib hier den XPATH")
    xpath = str(input())
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options)
    browser.get(url)
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        browser.add_cookie(cookie)
    text = browser.find_element_by_xpath(xpath).text
    print(text)
    browser.quit()
else:
    pass
if art == "write":
    print("Bitte schrieb hier die url rein")
    url = str(input())
    print("Schreib hier den XPATH")
    xpath = str(input())
    print("Schriebe hier den text hin")
    text = str(input())
    browser = webdriver.Firefox()
    browser.get(url)
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        browser.add_cookie(cookie)
    i = browser.find_element_by_xpath(xpath)
    i.send_keys(text)
    browser.quit()
else:
    pass
if art == "screenshot":
    print("Bitte schrieb hier die url rein")
    url = str(input())
    print("Schreib hier die id vom bild")
    xpath = str(input())
    print("schreibe hier was der name vom bild sein soll")
    name = str(input())
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options)
    browser.get(url)
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        browser.add_cookie(cookie)
    element = browser.find_element_by_id(xpath)
    location = element.location
    size = element.size
    browser.save_screenshot(name + ".png")
    browser.quit()
else:
    pass
if art == "load_cookies":
    print("Bitte schrieb hier die url rein")
    url = str(input())
    print("Schreib hier den XPATH")
    xpath = str(input())
    #options = Options()
    #options.headless = True
    # browser = webdriver.Firefox(options=options) #/html/body/div/c-wiz/div[2]/div/div/div/div/div[2]/form/div/span/span
    browser = webdriver.Firefox()
    browser.get(url)
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))).click()
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )

    pickle.dump(browser.get_cookies(), open("cookies.pkl", "wb"))
else:
    pass
