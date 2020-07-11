from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.
import time

phone_no = "xxxxxxxxxxxxxxxx"
driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com")

# We'll wait untill someone scanned the QR Code ...
search_box = WebDriverWait(driver, 10).until(
    expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div._3FRCZ.copyable-text.selectable-text"))
)
search_box.send_keys(phone_no)
# time.sleep(1000)
no_box = WebDriverWait(driver, 5).until(
    expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div._210SC"))
)
time.sleep(1)
no_box.click()
