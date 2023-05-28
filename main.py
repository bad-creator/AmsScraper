# подключаем Selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
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

driver.get(
    "https://jobs.ams.at/public/emps/jobs?page=1&query=Software-EntwicklerIn&location=wien&JOB_OFFER_TYPE=SB_WKO&JOB_OFFER_TYPE=IJ&JOB_OFFER_TYPE=BA&PERIOD=ALL&sortField=PERIOD")

# Проверка наличия всплывающего окна
popup_present = EC.presence_of_element_located((By.XPATH, '/html/body/sn-root/sn-cookie-banner/div/div/div'))

time.sleep(3)
# popup_decline_button = driver.find_element(By.CSS_SELECTOR, ".eom-button-row button:nth-child(1)")

popup_decline_button = driver.find_element(By.XPATH,
                                           '/html/body/sn-root/sn-cookie-banner/div/div/div/div[2]/div/div[2]/button')

popup_decline_button.click()

# Получаю список вакансий
vacancies_elements = driver.find_elements(By.CSS_SELECTOR, "#ams-search-result-list a[role='cell']:not([target='_blank'])")

# Получаю список ссылок на вакансии
vacancy_links = [vacancy.get_attribute('href') for vacancy in vacancies_elements]


for link in vacancy_links:
    time.sleep(1)
    driver.get(link)  # Переходим на страницу конкретной вакансии
    time.sleep(2)

    html = driver.find_element(By.ID, 'ams-detail-jobdescription-text').get_attribute('innerHTML')
    # Создаем объект BeautifulSoup для разбора HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Находим первый попавшийся элемент <a> с атрибутом href, содержащим "mailto:"
    email_element = soup.find('a', href=lambda href: href and href.startswith('mailto:'))

    if email_element:
        # Извлекаем адрес электронной почты
        email = email_element['href'][7:]
        # Выводим адрес электронной почты
        print(email)
    else:
        continue

    driver.back()  # Переходим назад на исходной вкладке
    time.sleep(1)
