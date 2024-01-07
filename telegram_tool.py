import csv
import pyperclip
from selenium.webdriver.support import expected_conditions as EC

import openpyxl
from selenium.webdriver.support.wait import WebDriverWait
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

import random


selenium.webdriver.support.select.Select
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


file_path = 'data.txt'
# Open the file in read mode
with open(file_path, 'r') as file:
    # Read the first line and assign it to a variable
    line1 = str(file.readline().strip())

    # Read the second line and assign it to another variable
    line2 = float(file.readline().strip())

    line3 = str(file.readline().strip())


PATH = "chromedriver.exe"
options = webdriver.ChromeOptions()
options.experimental_options["debuggerAddress"] = f"localhost:{line3}"
driver = webdriver.Chrome(PATH, options=options)
# driver.get("https://kingdomlikes.com/free_points/youtube-subscribe")
driver.maximize_window()
i = 0


# #################################################################
print(line1)
driver.get(line1)

# Open the file in read mode
with open('messages.txt', 'r') as file:
    # Read and print each line
    for line in file:
        # print(line.strip())  # strip() removes leading and trailing whitespaces (including the newline character)
        
        add_message = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='input-message-container']/div[1]")))
        driver.execute_script("arguments[0].scrollIntoView();", add_message)
        add_message.send_keys(line.strip())
        time.sleep(line2)
        send_message = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='btn-send-container']/button")))
        send_message.click()
        time.sleep(line2)
