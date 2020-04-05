#!/usr/bin/python3
from common import IPO
from selenium.webdriver.common.keys import Keys
import sys
import time

ipo = IPO('rakuten_boat')

try:
    ipo.driver.get('https://www.boatrace.jp/owpc/pc/login?authAfterUrl=/')
    ipo.driver.find_element_by_name("in_KanyusyaNo").send_keys(ipo.args.user)
    ipo.driver.find_element_by_name("in_AnsyoNo").send_keys(ipo.decrypt(ipo.args.password))
    ipo.driver.find_element_by_name("in_PassWord").send_keys(ipo.decrypt(ipo.args.password2))
    ipo.driver.find_element_by_xpath("//button[text()='ログインする']").click()
    ipo.driver.find_element_by_xpath("//a[text()='投票']").click()
    handle_array = ipo.driver.window_handles
    ipo.driver.switch_to.window(handle_array[-1])
    ipo.driver.find_element_by_xpath("//a/span[text()='入金・精算']").click()
    ipo.driver.find_element_by_xpath("//a[text()='入金する']").click()
    ipo.driver.find_element_by_id("chargeInstructAmt").send_keys('1')
    ipo.driver.find_element_by_id("chargeBetPassword").send_keys(ipo.decrypt(ipo.args.store))
    ipo.driver.find_element_by_xpath("//div[@id='payment']//a[text()='入金する']").click()
    ipo.driver.find_element_by_id("ok").click()
    time.sleep(5)
    ipo.driver.quit()
except:
    ipo.exit_on_err()
