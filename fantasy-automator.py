from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyinputplus as pyin 

browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
type(browser)

browser.get('https://fantasy.premierleague.com/my-team')


def login():
    login_element = browser.find_element_by_id("loginUsername")
    password_element = browser.find_element_by_id("loginPassword")

    print(login_element.is_displayed())
    print(password_element.is_displayed())

    login_element.send_keys("willrowston@gmail.com")
    password_element.send_keys(pyin.inputPassword())
    password_element.submit()

login()

def go_to_my_team_page():
    my_team = browser.find_element_by_link_text("My Team")
    my_team.click()

go_to_my_team_page()

