#!/usr/bin/python3
from common import IPO
from selenium.webdriver.common.keys import Keys
import sys

ipo = IPO('rakuten')

try:
    ipo.driver.get('https://www.rakuten-sec.co.jp/')
    ipo.driver.find_element_by_id("form-login-id").send_keys(ipo.args.user)
    ipo.driver.find_element_by_id("form-login-pass").send_keys(ipo.decrypt(ipo.args.password))
    ipo.driver.find_element_by_class_name("s3-form-login__btn").click()

    for i in range(5):
        ipo.driver.find_element_by_link_text("国内株式").click()
        ipo.driver.find_element_by_link_text("IPO（PO）に参加する").click()
        try:
            ipo.driver.find_element_by_xpath("//a[.='参加']").click()
        except:
            break
        ipo.driver.find_element_by_xpath("//input[contains(@value,'同意する')]").click()
        ipo.driver.find_element_by_name("value").send_keys('100')
        ipo.driver.find_element_by_name("price").click()
        ipo.driver.find_element_by_name("price").send_keys(Keys.ARROW_DOWN)
        ipo.driver.find_element_by_name("price").send_keys(Keys.ENTER)
        ipo.driver.find_element_by_xpath("//input[contains(@value,'確　認')]").click()
        ipo.driver.find_element_by_name("password").send_keys(ipo.decrypt(ipo.args.password2))
        ipo.screenshot()
        ipo.driver.find_element_by_xpath("//input[contains(@value,'参加申込')]").click()
        ipo.screenshot()
        print("楽天証券IPO("+str(i)+")に申し込みました", file=sys.stderr)
    
    ipo.driver.quit()
except:
    ipo.exit_on_err()
