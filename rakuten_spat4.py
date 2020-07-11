#!/usr/bin/python3
from common import Automation
from selenium.webdriver.common.keys import Keys
import sys
import time

a = Automation('rakuten_spat4')

try:
    a.driver.get('https://www.spat4.jp/keiba/pc')
    a.driver.find_element_by_id("MEMBERNUMR").send_keys(a.args.user)
    a.driver.find_element_by_id("MEMBERIDR").send_keys(a.decrypt(a.args.password))
    a.driver.find_element_by_xpath("//div[.='ログイン']").click()

#    a.driver.find_element_by_xpath("//input[@value='精算']").click()
#    a.driver.find_element_by_xpath("//input[@value='精算指示確認へ']").click()
#    a.driver.find_element_by_id("MEMBERPASSR").send_keys(a.decrypt(a.args.password2))
#    a.driver.find_element_by_xpath("//input[@value='精算指示する']").click()
#    time.sleep(30)
#except:
#    pass
#
#try:
    a.driver.find_element_by_xpath("//input[@value='入金']").click()
    handle_array = a.driver.window_handles
    a.driver.switch_to.window(handle_array[-1])
    a.driver.find_element_by_id("ENTERR").send_keys('100')
    a.driver.find_element_by_xpath("//input[@value='入金指示確認へ']").click()
    a.driver.find_element_by_id("MEMBERPASSR").send_keys(a.decrypt(a.args.password2))
    a.driver.find_element_by_xpath("//input[@value='入金指示する']").click()
    time.sleep(5)

    a.driver.quit()
except:
    a.exit_on_err()
