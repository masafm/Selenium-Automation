#!/usr/bin/env python3
from common import Automation
from selenium.webdriver.common.keys import Keys
import sys
import time

a = Automation('rakuten_boat')

try:
    a.driver.get('https://www.boatrace.jp/owpc/pc/login?authAfterUrl=/')
    a.driver.find_element_by_name("in_KanyusyaNo").send_keys(a.args.user)
    a.driver.find_element_by_name("in_AnsyoNo").send_keys(a.decrypt(a.args.password))
    a.driver.find_element_by_name("in_PassWord").send_keys(a.decrypt(a.args.password2))
    a.driver.find_element_by_xpath("//button[text()='ログインする']").click()
    a.driver.find_element_by_xpath("//a[text()='投票']").click()
    handle_array = a.driver.window_handles
    a.driver.switch_to.window(handle_array[-1])
    try:
        a.driver.find_element_by_id("newsoverviewdispCloseButton").click()
    except:
        pass
    a.driver.find_element_by_xpath("//a/span[text()='入金・精算']").click()
    a.driver.find_element_by_xpath("//a[text()='入金する']").click()
    a.driver.find_element_by_id("chargeInstructAmt").send_keys('1')
    a.driver.find_element_by_id("chargeBetPassword").send_keys(a.decrypt(a.args.store))
    a.driver.find_element_by_xpath("//div[@id='payment']//a[text()='入金する']").click()
    a.driver.find_element_by_id("ok").click()
    time.sleep(5)
    a.driver.quit()
except:
    a.exit_on_err()
