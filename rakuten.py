#!/usr/bin/env python3
from common import Automation
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import sys
import time

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
        element = a.driver.find_element_by_xpath("//input[contains(@value,'同意する')]")
        a.driver.execute_script("arguments[0].click();", element)
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
    
    for i in range(5):
        a.driver.find_element_by_link_text("国内株式").click()
        a.driver.find_element_by_link_text("IPO（PO）に参加する").click()
        try:
            a.driver.find_element_by_xpath("//a[.='申込']").click()
        except:
            break
        a.driver.find_element_by_xpath("//a[.='電子目論見書等一覧へ']").click()
        handle_array = a.driver.window_handles
        a.driver.switch_to.window(handle_array[-1])
        elements = a.driver.find_elements_by_xpath("//a[normalize-space(.)='閲覧']")
        for e in elements:
            href = e.get_attribute("href")
            script = f"window.open('{href}', '_blank');"
            a.driver.execute_script(script)
            time.sleep(1)
            handle_array = a.driver.window_handles
            a.driver.switch_to.window(handle_array[-1])
            iframe = a.driver.find_element_by_id("readframe")
            a.driver.switch_to.frame(iframe)
            time.sleep(1)
            a.driver.find_element_by_id("agreeMsg").click()
            time.sleep(1)
            a.driver.find_element_by_xpath("//a[normalize-space(.)='完了する']").click()
            a.driver.switch_to.default_content()
            time.sleep(1)
            a.driver.close()
        a.driver.close()
        handle_array = a.driver.window_handles
        a.driver.switch_to.window(handle_array[-1])
        driver.refresh()
        a.driver.find_element_by_xpath("//input[contains(@value,'確　認')]").click()
        a.driver.find_element_by_name("password").send_keys(a.decrypt(a.args.password2))
        a.driver.find_element_by_xpath("//input[contains(@value,'購入申込')]").click()
        a.screenshot()
        print("楽天証券IPO("+str(i)+")に購入申し込みしました", file=sys.stderr)
        
    a.driver.quit()
except:
    a.exit_on_err()
