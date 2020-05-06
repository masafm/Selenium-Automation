#!/usr/bin/python3
from common import Automation
from selenium.webdriver.common.keys import Keys
import sys
import time

a = Automation('rakuten_keiba')

try:
    a.driver.get('https://bet.keiba.rakuten.co.jp/bank/deposit/')
    a.driver.find_element_by_id("loginInner_u").send_keys(a.args.user)
    a.driver.find_element_by_id("loginInner_p").send_keys(a.decrypt(a.args.password))
    a.driver.find_element_by_class_name("loginButton").click()
    a.driver.find_element_by_id("depositingInputPrice").send_keys('100')
    a.driver.find_element_by_id("depositingInputButton").click()
    a.driver.find_element_by_name("pin").send_keys(a.decrypt(a.args.password2))
    a.driver.find_element_by_id("depositingConfirmButton").click()
    time.sleep(5)

    a.driver.quit()
except:
    a.exit_on_err()
