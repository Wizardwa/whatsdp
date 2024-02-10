#!/bin/python3 

import selenium
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import os


#store data and session
user_data = os.environ['chrome_user_data']
opt = webdriver.ChromeOptions()
opt.add_argument(f'--user-data-dir={user_data}')
opt.add_argument("--headless")

driver = webdriver.Chrome(options=opt)
driver.get("https://web.whatsapp.com")
time.sleep(30)

#click profile
print("Locating profile picture.....")
profile_header = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/header/div[1]/div").click()
time.sleep(2)
#open pictures folder
photo_path = "/home/ewaat/Pictures/4K"
contents = os.listdir(photo_path)
no_photos = len(contents)
count = 0
while count <= no_photos:
    try:
        photo = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[1]/span/div/span/div/div/div[1]/div/input")
        photo.send_keys(photo_path + '/' + contents[count])
        time.sleep(2)
        approve = driver.find_element(By.XPATH, "/html/body/div[1]/div/span[2]/div/div/div/div/div/div/div/div/div[2]/span/div/div").click()
        count = 2 + count
        time.sleep(60)
    except NoSuchElementException:
        pass









time.sleep(10)
