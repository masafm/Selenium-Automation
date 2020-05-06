#!/usr/bin/python3
from common import Automation
from selenium.webdriver.common.keys import Keys
import sys
import time

a = Automation('rakuten_e-shinbun')

try:
    a.driver.get('https://www.e-shinbun.net/account/?ref=ebet&path=http%3A%2F%2Fbet.e-shinbun.net%2F')
    a.driver.find_element_by_name("user[id]").send_keys(a.args.user)
    a.driver.find_element_by_name("user[pw]").send_keys(a.decrypt(a.args.password))
    a.driver.find_element_by_xpath("//a[.='ログイン']").click()
    a.driver.find_element_by_xpath("//img[@alt='入金']").click()
    a.driver.find_element_by_name("data[Statement][amount]").send_keys('100')
    a.driver.find_element_by_id("StatementNotice0").click()
    a.driver.find_element_by_xpath("//a[.='確認']").click()
    a.driver.find_element_by_name("data[User][password]").send_keys(a.decrypt(a.args.password2))
    a.driver.find_element_by_xpath("//a[.='実行']").click()
    time.sleep(5)
except:
    a.exit_on_err()

a.driver.quit()
