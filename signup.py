from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait

# get login info from file
f = open("login.txt", "r")
username = f.readline()
password = f.readline()

# navigating to shift sign-up page
browser = webdriver.Chrome('C:/Users/smili/Downloads/chromedriver.exe')
browser.maximize_window()
browser.get('https://na.amazonmoment.com/goa/wfm/associate/schedule')
browser.find_element_by_id('usernameInputField').send_keys(username)
browser.find_element_by_class_name('a-button-input').click()
browser.find_element_by_id('passwordInputField').send_keys(password)
browser.find_element_by_class_name('a-button-input').click()
browser.get('https://na.amazonmoment.com/goa/wfm/associate/adjustments')
browser.implicitly_wait(10)

# finding shifts
div = browser.find_element_by_class_name('card-block')
sign_up_table = div.find_element_by_class_name('table-striped')

rows = sign_up_table.find_elements_by_tag_name('tr')
for row in rows:
    print(row.text)
    # cols = row.find_elements_by_tag_name('td')
    # if cols[2].text.find('2020-08-17T04:00'):
    #     cols[4].find_element_by_tag_name('button').click()
    #     break

