#!/usr/bin/python3
from common import Automation
from selenium.webdriver.common.keys import Keys
import sys
import time

a = Automation('rakuten_chariloto')

try:
    a.driver.get('https://www.chariloto.com/login?new=1')
    a.driver.find_element_by_id("chariloto_id").send_keys(a.args.user)
    a.driver.find_element_by_id("password").send_keys(a.decrypt(a.args.password))
    a.driver.find_element_by_xpath("//button/i[@class='ico ico-key']").click()
    a.driver.find_element_by_xpath("//a//span[contains(text(), '入金')]").click()
    a.driver.find_element_by_id("js-input").send_keys('10')
    a.driver.find_element_by_xpath("//input[@value='確認']").click()
    a.driver.find_element_by_id("mypage_bank_statement_deposit_form_pincode").send_keys(a.decrypt(a.args.password2))
    a.driver.find_element_by_xpath("//input[@value='実行']").click()
    time.sleep(5)
except:
    a.exit_on_err()

a.driver.quit()
