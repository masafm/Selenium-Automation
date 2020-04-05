#!/usr/bin/python3
from common import IPO
from selenium.webdriver.common.keys import Keys
import sys
import time

ipo = IPO('rakuten_auto')

try:
    ipo.driver.get('https://pc.autoinet.jp/')
    ipo.driver.find_element_by_name("userId").send_keys(ipo.args.user)
    ipo.driver.find_element_by_name("password").send_keys(ipo.decrypt(ipo.args.password))
    ipo.driver.find_element_by_name("login").click()
    time.sleep(1)
    ipo.driver.find_element_by_name("passNo").send_keys(ipo.decrypt(ipo.args.password2))
    ipo.driver.find_element_by_name("btnWireOut").click()
    time.sleep(1)
    ipo.driver.find_element_by_name("wireOutAmount").send_keys('100')
    ipo.driver.find_element_by_name("refer").click()
    time.sleep(1)
    ipo.driver.switch_to.alert.accept()
    time.sleep(5)
except:
    pass

try:
    ipo.driver.get('https://pc.autoinet.jp/')
    ipo.driver.find_element_by_name("userId").send_keys(ipo.args.user)
    ipo.driver.find_element_by_name("password").send_keys(ipo.decrypt(ipo.args.password))
    ipo.driver.find_element_by_name("login").click()
    time.sleep(1)
    ipo.driver.find_element_by_name("passNo").send_keys(ipo.decrypt(ipo.args.password2))
    ipo.driver.find_element_by_name("btnWireIn").click()
    time.sleep(1)
    ipo.driver.find_element_by_name("wireInAmount").send_keys('1')
    ipo.driver.find_element_by_name("refer").click()
    time.sleep(1)
    ipo.driver.switch_to.alert.accept()
    time.sleep(5)
except:
    ipo.exit_on_err()

ipo.driver.quit()
