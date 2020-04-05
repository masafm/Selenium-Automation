#!/usr/bin/python3
from common import IPO
from selenium.webdriver.common.keys import Keys
import sys
import time

ipo = IPO('rakuten_keiba')

try:
    ipo.driver.get('https://bet.keiba.rakuten.co.jp/bank/deposit/')
    ipo.driver.find_element_by_id("loginInner_u").send_keys(ipo.args.user)
    ipo.driver.find_element_by_id("loginInner_p").send_keys(ipo.decrypt(ipo.args.password))
    ipo.driver.find_element_by_class_name("loginButton").click()
    ipo.driver.find_element_by_id("depositingInputPrice").send_keys('100')
    ipo.driver.find_element_by_id("depositingInputButton").click()
    ipo.driver.find_element_by_name("pin").send_keys(ipo.decrypt(ipo.args.password2))
    ipo.driver.find_element_by_id("depositingConfirmButton").click()
    time.sleep(5)

    ipo.driver.quit()
except:
    ipo.exit_on_err()
