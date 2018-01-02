#!/usr/bin/env python

from selenium import webdriver
from getpass import getpass
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from pprint import pprint

with open('editettava.json') as data_file:
    data = json.load(data_file)

usr = data["infos"][0]["email"]
pwd = data["infos"][1]["password"]
t = int(data["time"][0]["toisto"])
t2 = int(data["time"][1]["bumppiaika"])

# choose your own path for chromedriver
driver = webdriver.Chrome('/home/bora/Desktop/chromedriver')
driver.get(data["address"][0]["urli"])

wait = WebDriverWait(driver, 10)

wait.until(EC.visibility_of_element_located((By.NAME, 'username')))
usr_box = driver.find_element_by_name('username')
usr_box.send_keys(usr)
sleep(3)

pwd_box = driver.find_element_by_name('password')
pwd_box.send_keys(pwd)
sleep(3)

login_button = driver.find_element_by_xpath('.//form[@class="login"][contains(., "Login")]')
login_button.submit()
sleep(3)


driver.get(data["address"][1]["lanka"])
count = 0
while (count < t):
	wait = WebDriverWait(driver, 10)
	wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'forcebump')))
	bump_box = driver.find_element_by_xpath('.//button[@class="forcebump linkbutton"][contains(., "Force bump")]').click()
	sleep(3)
	alert = driver.switch_to.alert
	alert.accept()
	sleep(3)
	alert = driver.switch_to.alert
	alert.accept()
	driver.get(data["address"][1]["lanka"])
	sleep(t2)
	count = count + 1

