#!/usr/bin/python3
from common import IPO
from selenium.webdriver.common.keys import Keys
import sys
import time

ipo = IPO('rakuten_oddspark')

try:
    ipo.driver.get('https://www.oddspark.com/OpTop.do?SSO_FORCE_LOGIN=1&SSO_URL_RETURN=https://www.oddspark.com/')
    ipo.driver.find_element_by_name("SSO_ACCOUNTID").send_keys(ipo.args.user)
    ipo.driver.find_element_by_name("SSO_PASSWORD").send_keys(ipo.decrypt(ipo.args.password))
    ipo.driver.execute_script("formSubmit();")
    try:
        ipo.driver.find_element_by_name("INPUT_PIN").send_keys(ipo.decrypt(ipo.args.password2))
        ipo.driver.find_element_by_name("送信").click()
    except:
        pass
    ipo.driver.get('https://www.oddspark.com/auth/NyukinMenu.do')    
    ipo.driver.find_element_by_xpath("//a[.='精算する']").click()
    ipo.driver.find_element_by_name("touhyoPassword").send_keys(ipo.decrypt(ipo.args.password2))
    ipo.driver.find_element_by_xpath("//a[.='精算']").click()
    time.sleep(5)
except:
    pass

try:
    ipo.driver.get('https://www.oddspark.com/OpTop.do?SSO_FORCE_LOGIN=1&SSO_URL_RETURN=https://www.oddspark.com/')
    ipo.driver.find_element_by_name("SSO_ACCOUNTID").send_keys(ipo.args.user)
    ipo.driver.find_element_by_name("SSO_PASSWORD").send_keys(ipo.decrypt(ipo.args.password))
    ipo.driver.execute_script("formSubmit();")
    try:
        ipo.driver.find_element_by_name("INPUT_PIN").send_keys(ipo.decrypt(ipo.args.password2))
        ipo.driver.find_element_by_name("送信").click()
    except:
        pass
    ipo.driver.get('https://www.oddspark.com/auth/NyukinMenu.do')    
    ipo.driver.find_element_by_xpath("//a[.='入金する']").click()
    ipo.driver.find_element_by_name("nyukin").send_keys('1')
    ipo.driver.find_element_by_xpath("//a[.='次へ']").click()
    ipo.driver.find_element_by_name("touhyoPassword").send_keys(ipo.decrypt(ipo.args.password2))
    ipo.driver.find_element_by_xpath("//a[.='入金']").click()
    time.sleep(5)
except:
    ipo.exit_on_err()

ipo.driver.quit()
