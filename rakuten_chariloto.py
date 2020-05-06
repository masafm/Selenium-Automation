#!/usr/bin/python3
from common import IPO
from selenium.webdriver.common.keys import Keys
import sys
import time

ipo = IPO('rakuten_chariloto')

try:
    ipo.driver.get('https://www.chariloto.com/login?new=1')
    ipo.driver.find_element_by_id("chariloto_id").send_keys(ipo.args.user)
    ipo.driver.find_element_by_id("password").send_keys(ipo.decrypt(ipo.args.password))
    ipo.driver.find_element_by_xpath("//button/i[@class='ico ico-key']").click()
    ipo.driver.find_element_by_xpath("//a//span[contains(text(), '入金')]").click()
    ipo.driver.find_element_by_id("js-input").send_keys('10')
    ipo.driver.find_element_by_xpath("//input[@value='確認']").click()
    ipo.driver.find_element_by_id("mypage_bank_statement_deposit_form_pincode").send_keys(ipo.decrypt(ipo.args.password2))
    ipo.driver.find_element_by_xpath("//input[@value='実行']").click()
    time.sleep(5)
except:
    ipo.exit_on_err()

ipo.driver.quit()
