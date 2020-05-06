#!/usr/bin/python3
from common import IPO
from selenium.webdriver.common.keys import Keys
import sys
import time

ipo = IPO('rakuten_e-shinbun')

try:
    ipo.driver.get('https://www.e-shinbun.net/account/?ref=ebet&path=http%3A%2F%2Fbet.e-shinbun.net%2F')
    ipo.driver.find_element_by_name("user[id]").send_keys(ipo.args.user)
    ipo.driver.find_element_by_name("user[pw]").send_keys(ipo.decrypt(ipo.args.password))
    ipo.driver.find_element_by_xpath("//a[.='ログイン']").click()
    ipo.driver.find_element_by_xpath("//img[@alt='入金']").click()
    ipo.driver.find_element_by_name("data[Statement][amount]").send_keys('100')
    ipo.driver.find_element_by_id("StatementNotice0").click()
    ipo.driver.find_element_by_xpath("//a[.='確認']").click()
    ipo.driver.find_element_by_name("data[User][password]").send_keys(ipo.decrypt(ipo.args.password2))
    ipo.driver.find_element_by_xpath("//a[.='実行']").click()
    time.sleep(5)
except:
    ipo.exit_on_err()

ipo.driver.quit()
