#!/usr/bin/python3
from common import Automation
from selenium.webdriver.common.keys import Keys
import sys
import time

a = Automation('rakuten_auto_out')

try:
    a.driver.get('https://pc.autoinet.jp/')
    a.driver.find_element_by_name("userId").send_keys(a.args.user)
    a.driver.find_element_by_name("password").send_keys(a.decrypt(a.args.password))
    a.driver.find_element_by_name("login").click()
    time.sleep(1)
    a.driver.find_element_by_name("passNo").send_keys(a.decrypt(a.args.password2))
    a.driver.find_element_by_name("btnWireOut").click()
    time.sleep(1)
    a.driver.find_element_by_name("wireOutAmount").send_keys('700')
    a.driver.find_element_by_name("refer").click()
    time.sleep(1)
    a.driver.switch_to.alert.accept()
    time.sleep(5)
except:
    a.exit_on_err()

a.driver.quit()
