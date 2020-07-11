#!/usr/bin/python3
from common import Automation
from selenium.webdriver.common.keys import Keys
import sys
import time

a = Automation('rakuten_spat4_out')

try:
    a.driver.get('https://www.spat4.jp/keiba/pc')
    a.driver.find_element_by_id("MEMBERNUMR").send_keys(a.args.user)
    a.driver.find_element_by_id("MEMBERIDR").send_keys(a.decrypt(a.args.password))
    a.driver.find_element_by_xpath("//div[.='ログイン']").click()

    a.driver.find_element_by_xpath("//input[@value='精算']").click()
    a.driver.find_element_by_xpath("//input[@value='精算指示確認へ']").click()
    a.driver.find_element_by_id("MEMBERPASSR").send_keys(a.decrypt(a.args.password2))
    a.driver.find_element_by_xpath("//input[@value='精算指示する']").click()
    time.sleep(5)

    a.driver.quit()
except:
    a.exit_on_err()
