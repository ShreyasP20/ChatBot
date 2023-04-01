from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyperclip
import time

browser = webdriver.Chrome( executable_path='C:\\Users\\Lucifer Jones\\Appdata\\Local\\Google\\Chrome\\User Data\\Wtsp')
browser.get('https://web.whatsapp.com/')
time.sleep(5)
search_xpath='//span[@data-testid="last-msg-status"]'
read_title=WebDriverWait(browser, 500).until(
          EC.presence_of_element_located((By.XPATH, search_xpath))
         )
mesgs=browser.find_elements("xpath",search_xpath)
for i in mesgs:
    #print(type(i.text))
    single_msg=i.text
    reply_msg=single_msg.split(":")
    if len(reply_msg) > 1:
        print(reply_msg[1])
    elif len(reply_msg) < 1:
        print(reply_msg[0])