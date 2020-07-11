from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import random
import string

gmail_url = """https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default&flowName=GlifWebSignIn&flowEntry=SignUp"""
data = [
    ("monika", "ritviza")
]
no_set = "0123456789"

def generateRandom():
    """
    Description: This method is used to create a random 5 digit no.
    Return: no (str)
    """
    temp = ""
    for i in range(5):
        temp += no_set[random.randint(0, len(no_set)-1)]
    return temp

driver = webdriver.Firefox()
driver.get(gmail_url)

# Filling the form...
random_digit = generateRandom()
first_name_input = driver.find_element_by_css_selector("input#firstName")
first_name_input.send_keys(data[0][0])

last_name_input = driver.find_element_by_css_selector("input#lastName")
last_name_input.send_keys(data[0][1])

username_input = driver.find_element_by_css_selector("input#username")
username_input.send_keys(data[0][0]+data[0][1]+'.'+random_digit)

password_input = driver.find_element_by_css_selector("input[name='Passwd']")
password_input.send_keys(random_digit*2)

confirm_password_input = driver.find_element_by_css_selector("input[name='ConfirmPasswd']")
confirm_password_input.send_keys(random_digit*2)

data_file = open('data.txt', 'a')
data_file.write(data[0][0]+data[0][1]+'.'+random_digit+' '+random_digit*2+'\n')
data_file.close()

next_btn = driver.find_element_by_css_selector("span.RveJvd.snByac")
next_btn.click()

phone_input = driver.find_element_by_css_selector("input#phoneNumberId")
phone_input.send_keys("9354085897")

next_btn = driver.find_element_by_css_selector("span.RveJvd.snByac")
next_btn.click()

verification_code = input(">>> Enter the Code: ")

phone_input = driver.find_element_by_css_selector("input#code")
phone_input.send_keys(verification_code)

next_btn = driver.find_elements_by_css_selector("span.RveJvd.snByac")[1]
next_btn.click()

phone_input = WebDriverWait(driver, 10).until(
    expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input#phoneNumberId"))
)
phone_input.clear()

day_input = driver.find_element_by_css_selector("input#day")
day_input.send_keys(str(random.randint(1, 20)))

month_input = driver.find_element_by_css_selector("select#month")
month_options = month_input.find_elements_by_tag_name('option')
month_options[0].click()

year_input = driver.find_element_by_css_selector("input#month")
year_input.send_keys("2000")

gender_input = driver.find_element_by_css_selector("select#gender")
gender_options = month_input.find_elements_by_tag_name('option')
gender_options[0].click()

next_btn = driver.find_elements_by_css_selector("span.RveJvd.snByac")[1]
next_btn.click()
