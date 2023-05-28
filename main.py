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

driver.get("https://jobs.ams.at/public/emps/jobs?page=1&query=Software-EntwicklerIn&location=wien&JOB_OFFER_TYPE=SB_WKO&JOB_OFFER_TYPE=IJ&JOB_OFFER_TYPE=BA&PERIOD=ALL&sortField=PERIOD")

# Проверка наличия всплывающего окна
popup_present = EC.presence_of_element_located((By.XPATH, '/html/body/sn-root/sn-cookie-banner/div/div/div'))

time.sleep(5)
# popup_decline_button = driver.find_element(By.CSS_SELECTOR, ".eom-button-row button:nth-child(1)")

popup_decline_button = driver.find_element(By.XPATH, '/html/body/sn-root/sn-cookie-banner/div/div/div/div[2]/div/div[2]/button')

popup_decline_button.click()

time.sleep(15)
