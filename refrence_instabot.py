from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import random
import time
import pickle

firefox_options = FirefoxProfile()
firefox_options.set_preference(
    "general.useragent.override", 
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/12.0 Mobile/15A372 Safari/604.1"
)

driver = webdriver.Firefox(firefox_profile=firefox_options)
driver.get("https://instagram.com")

with open("credentials.cred", "rb") as file:
    data = pickle.load(file)
    username, password = data['username'], data['password']
    
def bot_log(text):
    print("[+] InstaBot:", text)

def login(username, password):
    """
    URL_NEEDED: http://instagram.com
    Adding Soon...
    """
    driver.find_element_by_css_selector("button.sqdOP.L3NKy.y3zKF[type='button']").click()
    username_input = driver.find_element_by_css_selector("input[name='username']")
    password_input = driver.find_element_by_css_selector("input[name='password']")
    username_input.clear()
    username_input.send_keys(username)
    password_input.clear()
    password_input.send_keys(password)
    driver.find_element_by_css_selector("button.sqdOP.L3NKy.y3zKF[type='submit']").click()
    try:
        save_btn = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "button.sqdOP.L3NKy.y3zKF[type='button']"))
        )
        save_btn.click()
    except:
        bot_log("Save Info Button is not loading.")
    
# login(username, password)

def search(query):
    """
    Adding Soon...
    """
    driver.find_element_by_css_selector("a.gKAyB[href='/explore/']").click()
    # Handling the search button...
    search_input = driver.find_element_by_css_selector("input.j_2Hd.iwQA6.RO68f.M5V28[placeholder='Search']")
    search_input.click()
    search_input.clear()
    search_input.send_keys([query])
    time.sleep(3)
    # We need to wait untill the AJAXify search menu appears then 
    # We'will click on the first one.
    # driver.find_element_by_css_selector("div.fuqBx a.yCE8d").click()
    # Let's use Web DriverWait instead of time.sleep()
    req_a = WebDriverWait(driver, 3).until(
        expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "li a.-qQT3"))
    )
    req_a.click()
search("#100daysofcode")


# PROJECT ON INSTAGRAM BOT
# @author: @VIVEKASCODER
# VARSION: 1.0.1 beta
# SOLELY CREATED BY AUTHOR.

"""
MAIL_ME: PBQRE@PM.ME
FEATURES:
	> LIKE POST BASED ON TOP HASHTAGS SCRAPED FROM INTERNET
	> COMMENT ON THEM.
	> ...
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from requests_html import HTMLSession
import pickle
import time
import random

with open("creadentials.cred", "rb") as file:
    data = pickle.loads(file.read())
    username, password = data["username"], data["password"]

trending_keywords = []
base_comments = [
    "❤", "🥺", "✨", "🥰", "✨", "😊", "😍", "🏆", "🔥", "☀", "💕",
    "Coolest Post.",
    "Nice Post 🔥",
    "OMG Post.",
    "Nice", "Great Post 🏆"
]


file = open("trending_keywords.txt", "w+")
for i in trending_keyword:
    file.write(i+"\n")
print("All Done [*_*]")

driver = webdriver.Firefox()
driver.get("https://instagram.com/")


def login_and_save():
	driver.find_element_by_css_selector("input[name='username']").clear()
	driver.find_element_by_css_selector("input[name='password']").clear()
	driver.find_element_by_css_selector("input[name='username']").send_keys(username)
	driver.find_element_by_css_selector("input[name='password']").send_keys(password)
	driver.find_element_by_css_selector("button.sqdOP.L3NKy.y3zKF[type='submit']").click()

	# Saving the accoung login info btn handler...
	driver.find_element_by_css_selector("button.sqdOP.L3NKy.y3zKF[type='button']").click()


# Handling the search button...
def search_hashtag(hashtag):
    """
    This function will search a give hashtag...
    """
    search_input = driver.find_element_by_css_selector("input.XTCLo.x3qfX[placeholder='Search']")
    search_input.clear()
    search_input.send_keys([hashtag])
    time.sleep(3)
    # We need to wait untill the AJAXify search menu appears then 
    # We'will click on the first one.
    # driver.find_element_by_css_selector("div.fuqBx a.yCE8d").click()
    # Let's use Web DriverWait instead of time.sleep()
    req_a = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div.fuqBx a.yCE8d"))
    )
    req_a.click()
    

def like_hashtag_page(no_of_posts):
    """
    This function will try to find the clickable posts on the 
    current url, and click on the very first post.
    """
    liked_color = "#ed4956"
    normal_color = "#262626"
	# driver.find_elements_by_css_selector("div.v1Nh3.kIKUG._bz0w")[0].click()
    post = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div.v1Nh3.kIKUG._bz0w"))
    )
    post.click()
    # like_btn = driver.find_element_by_css_selector("span.fr66n button.wpO6b")
    if no_of_posts != "__all__":
        for i in range(no_of_posts):
            next_btn = driver.find_element_by_css_selector("a._65Bje.coreSpriteRightPaginationArrow")
            like_btn = WebDriverWait(driver, 10).until(
                expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.fr66n button.wpO6b"))
            )
            color = driver.find_element_by_css_selector("div.QBdPU  span svg._8-yf5").get_attribute("fill")
            if color == normal_color:
                like_btn.click()
            else:
                print("[BOT_LOG]: FOUND POST ALREADY LIKED.")
            next_btn.click()
    else:
        while True:
            next_btn = driver.find_element_by_css_selector("a._65Bje.coreSpriteRightPaginationArrow")
            like_btn = WebDriverWait(driver, 10).until(
                expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.fr66n button.wpO6b"))
            )
            color = driver.find_element_by_css_selector("div.QBdPU  span svg._8-yf5").get_attribute("fill")
            if color == normal_color:
                like_btn.click()
            else:
                print("[BOT_LOG]: FOUND POST ALREADY LIKED.")
            next_btn.click()


def scrap_hashtags():     
	url = "https://top-hashtags.com/instagram/"
	trending_keyword = []

	session = HTMLSession()
	for i in range(22):
	    if i != 0:
	        url += str(i)+"01/"
	    r = session.get(url)
	    a_s = r.html.find("div.i-tag a", first=False)
	    for a in a_s:
	        trending_keyword.append(a.text)
	  

def scrap_comments():
    """
    URL: https://www.trendingus.com/comments-for-girls/
    This function scraps some of the best comments from the internet.
    """
    r = session.get("https://www.trendingus.com/comments-for-girls/")
    li_s = r.html.find("ol li", first=False)
    for li in li_s:
        comments.append(li.text + ", Just Kidding 😊")
	scrap_comments()
	print(comments, "\nLength: ", len(comments))  

def give_random_hashtag():
    return trending_keyword[random.randint(0, len(trending_keyword)-1)]


def generate_random_comment_emoji_list(emoji_list, length_of_comment, no_of_comments):
    """
    emoji_list: a list of emoji from which we generate the comment
    length_of_comment: self explanatory...
    no_of_comments: no of comments you wanna generate
    """
    comment_list = []
    for j in range(no_of_comments):
        comment = ""
        for i in range(length_of_comment):    
            comment += emoji_list[random.randint(0, len(emoji_list)-1)]
        comment_list.append(comment)
    return comment_list


def execute_on(hashtag):
	search_hashtag(hashtag)
	time.sleep(5)
	count = like_hashtag_page(
	    no_of_posts="__all__", 
	    comments=generate_random_comment_emoji_list(
	        emoji_list=["❤", "🥺", "✨", "🥰", "✨", "😊", "😍", "🏆", "🔥", "☀", "💕"], 
	        length_of_comment=5, 
	        no_of_comments=1000
	    ), 
	    percentage_of_comments=5
	)
	print(count)
