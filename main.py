# подключаем Selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# подключаем библиотеку для работы с Excel
import openpyxl

# подключаем библиотеку для работы с файлами
import os

# подключаем библиотеку для работы с датой
import datetime

# подключаем библиотеку для работы с регулярными выражениями
import re

driver = webdriver.Chrome('venv/chromedriver_mac64/chromedriver')

driver.get("https://www.youtube.com/")

# Проверка наличия всплывающего окна
popup_present = EC.presence_of_element_located((By.XPATH, '//*[@id="dialog"]'))

time.sleep(5)
# popup_decline_button = driver.find_element(By.CSS_SELECTOR, ".eom-button-row button:nth-child(1)")

popup_decline_button = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[6]/div[1]/ytd-button-renderer[1]')

popup_decline_button.click()

time.sleep(10)
