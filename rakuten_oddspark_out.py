#!/usr/bin/env python3
from common import Automation
from selenium.webdriver.common.keys import Keys
import sys
import time

a = Automation('rakuten_oddspark_out')

try:
    a.driver.get('https://www.oddspark.com/OpTop.do?SSO_FORCE_LOGIN=1&SSO_URL_RETURN=https://www.oddspark.com/')
    a.driver.find_element_by_name("SSO_ACCOUNTID").send_keys(a.args.user)
    a.driver.find_element_by_name("SSO_PASSWORD").send_keys(a.decrypt(a.args.password))
    a.driver.execute_script("formSubmit();")
    try:
        a.driver.find_element_by_name("INPUT_PIN").send_keys(a.decrypt(a.args.password2))
        a.driver.find_element_by_name("送信").click()
    except:
        pass

    a.driver.get('https://www.oddspark.com/auth/NyukinMenu.do')
    a.driver.find_element_by_xpath("//a[.='精算する']").click()
    a.driver.find_element_by_name("touhyoPassword").send_keys(a.decrypt(a.args.password2))
    a.driver.find_element_by_xpath("//a[.='精算']").click()
    time.sleep(5)

    a.driver.quit()
except:
    a.exit_on_err()

