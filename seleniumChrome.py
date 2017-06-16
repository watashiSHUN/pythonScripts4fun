#! /usr/bin/env python3
import time
from selenium import webdriver
import pickle

with open("data.pickle","rb") as f:
    dic = pickle.load(f)
print(dic)

userNameInput = dic["userName"]
passWordInput = dic["passWord"]

driver = webdriver.Chrome('/home/watashishun/Downloads/chromeDriver26/chromedriver')
driver.implicitly_wait(10000) # seconds
# needed
driver.get('https://www.bing.com')
# first, try to login

idElement = driver.find_element_by_id("id_l") # hp_id_hdr is displayed
time.sleep(1) # if not, this is not displayed
idElement.click()

classElement = driver.find_element_by_class_name("b_toggle")
classElement.click()
# new page for login
userName = driver.find_element_by_name("loginfmt")
userName.send_keys(userNameInput)

nextButton = driver.find_element_by_id("idSIButton9")
nextButton.click()
time.sleep(1)

passWord = driver.find_element_by_name("passwd")
passWord.send_keys(passWordInput)
passWord.submit()
time.sleep(1)

# search
test = ["steam","motion","path","liquid","log","meant","quotient","teeth","shell","neck"]
for t in test:
    iElem = driver.find_element_by_id("sb_form_q")
    iElem.clear()
    iElem.send_keys(t)
    iElem.submit()
    time.sleep(1)

driver.quit()
