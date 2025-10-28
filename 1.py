from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

import logging
logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w")

import os
from dotenv import load_dotenv
load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

try:
    logging.info("Запуск программы ...")
    firefox_options = Options()
    firefox_options.page_load_strategy = 'eager'

    driver = webdriver.Firefox(options=firefox_options)
    url = "https://secure.veesp.com/clientarea?_gl=1*122iupy*_ga*MTg3MjE3MDE3My4xNzU4MTAzNDEw*_ga_CNPR3KX8TF*czE3NjE2MzQ5NDgkbzIkZzEkdDE3NjE2MzQ5NjYkajQyJGwwJGgw"
    driver.get(url)

    wait = WebDriverWait(driver, 10)

    email_form = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    email_form.send_keys(EMAIL)
    logging.info("Введена почта")

    passwd_form = driver.find_element(By.NAME, "password")
    passwd_form.send_keys(PASSWORD)
    logging.info("Введен пароль")

    enter_button = driver.find_element(By.XPATH, '//button[text()="Вход"]')
    enter_button.click()
    logging.info("Вход выполнен успешно")
except Exception as e:
    logging.error(f"Ошибка: {e}")

finally:
    if 'driver' in locals():
        driver.quit()
        logging.info("Браузер закрыт")