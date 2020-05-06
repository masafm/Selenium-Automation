#!/usr/bin/python3
from common import Automation
from selenium.webdriver.common.keys import Keys
import sys

a = Automation('rakuten')

try:
    a.driver.get('https://www.rakuten-sec.co.jp/')
    a.driver.find_element_by_id("form-login-id").send_keys(a.args.user)
    a.driver.find_element_by_id("form-login-pass").send_keys(a.decrypt(a.args.password))
    a.driver.find_element_by_class_name("s3-form-login__btn").click()

    for i in range(5):
        a.driver.find_element_by_link_text("国内株式").click()
        a.driver.find_element_by_link_text("IPO（PO）に参加する").click()
        try:
            a.driver.find_element_by_xpath("//a[.='参加']").click()
        except:
            break
        a.driver.find_element_by_xpath("//input[contains(@value,'同意する')]").click()
        a.driver.find_element_by_name("value").send_keys('100')
        a.driver.find_element_by_name("price").click()
        a.driver.find_element_by_name("price").send_keys(Keys.ARROW_DOWN)
        a.driver.find_element_by_name("price").send_keys(Keys.ENTER)
        a.driver.find_element_by_xpath("//input[contains(@value,'確　認')]").click()
        a.driver.find_element_by_name("password").send_keys(a.decrypt(a.args.password2))
        a.screenshot()
        a.driver.find_element_by_xpath("//input[contains(@value,'参加申込')]").click()
        a.screenshot()
        print("楽天証券IPO("+str(i)+")に申し込みました", file=sys.stderr)
    
    a.driver.quit()
except:
    a.exit_on_err()
