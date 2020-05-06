#!/usr/bin/python3
from common import IPO
from selenium.webdriver.common.keys import Keys
import sys
import time

ipo = IPO('rakuten_spat4')

try:
    ipo.driver.get('https://www.spat4.jp/keiba/pc')
    ipo.driver.find_element_by_id("MEMBERNUMR").send_keys(ipo.args.user)
    ipo.driver.find_element_by_id("MEMBERIDR").send_keys(ipo.decrypt(ipo.args.password))
    ipo.driver.find_element_by_xpath("//div[.='ログイン']").click()
    ipo.driver.find_element_by_xpath("//input[@value='入金']").click()
    handle_array = ipo.driver.window_handles
    ipo.driver.switch_to.window(handle_array[-1])    
    ipo.driver.find_element_by_id("ENTERR").send_keys('100')
    ipo.driver.find_element_by_xpath("//input[@value='入金指示確認へ']").click()
    ipo.driver.find_element_by_id("MEMBERPASSR").send_keys(ipo.decrypt(ipo.args.password2))
    ipo.driver.find_element_by_xpath("//input[@value='入金指示する']").click()
    time.sleep(5)

    ipo.driver.quit()
except:
    ipo.exit_on_err()
