from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# get login info from file
f = open("login.txt", "r")
username = f.readline()
password = f.readline()

# navigating to shift sign-up page
browser = webdriver.Chrome('C:/Users/smili/Downloads/chromedriver.exe')
browser.get('https://na.amazonmoment.com/goa/wfm/associate/schedule')
browser.find_element_by_id('usernameInputField').send_keys(username)
browser.find_element_by_class_name('a-button-input').click()
browser.find_element_by_id('passwordInputField').send_keys(password)
browser.find_element_by_class_name('a-button-input').click()
browser.get('https://na.amazonmoment.com/goa/wfm/associate/adjustments')
WebDriverWait(browser,10)

# finding available shifts
avail_shifts_times = browser.find_elements_by_class_name('hidden-sm-down')
for i in avail_shifts_times:
    print("Element is", i.text, "\n")

