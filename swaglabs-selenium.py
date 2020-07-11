"""
I wanted to buy a jacket, but i dont wanna use my hands, so let's use selenium
Author: @vivekascoder
Email: pbqre@protonmail.com
"""

#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# General information to be filled on the site.
# --> Not real off course.
username = "standard_user"
password = "secret_sauce"
first_name = "vivek"
last_name = "kumar"
postal_code = "110043"

driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com/")

# Taking care of login section
username_box = driver.find_element_by_css_selector("input[data-test='username']")
password_box = driver.find_element_by_css_selector("input[data-test='password']")
username_box.send_keys(username)
password_box.send_keys(password)
login_btn = driver.find_element_by_css_selector("input.btn_action")
login_btn.click()

# Trying to fetch all products ...
items = driver.find_elements_by_css_selector("div.inventory_item_name")
buttons = driver.find_elements_by_css_selector("button.btn_primary.btn_inventory")
for item in items:
    print(item.text)
    if "Jacket" in item.text:
        button = buttons[items.index(item)]
        button.click()

# Going to checkout section.
checkout_btn = driver.find_element_by_css_selector("a.shopping_cart_link.fa-layers.fa-fw")
checkout_btn.click()
final_checkout_btn = driver.find_element_by_css_selector("a.btn_action.checkout_button")
final_checkout_btn.click()

firstname_box = driver.find_element_by_css_selector("input[data-test='firstName']")
firstname_box.send_keys(first_name)
lastname_box = driver.find_element_by_css_selector("input[data-test='lastName']")
lastname_box.send_keys(last_name)
postal_box = driver.find_element_by_css_selector("input[data-test='postalCode']")
postal_box.send_keys(postal_code)

# Finally ...
order_btn = driver.find_element_by_css_selector("input.btn_primary.cart_button")
order_btn.click()
finish_btn = driver.find_element_by_css_selector("a.btn_action.cart_button")
finish_btn.click()

