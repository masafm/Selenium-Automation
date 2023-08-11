#!/usr/bin/env python3
from common import Automation
import sys
import time

a = Automation('sbi')

try:
    a.driver.get('https://www.sbisec.co.jp/')
    a.driver.find_element_by_name("user_id").send_keys(a.args.user)
    a.driver.find_element_by_name("user_password").send_keys(a.decrypt(a.args.password))
    a.driver.find_element_by_name("ACT_login").click()
    time.sleep(3)
    
    for i in range(5):
        a.driver.find_element_by_xpath("//img[@alt='ホーム']").click()
        a.driver.find_element_by_xpath("//img[@alt='国内株式']").click()
        a.driver.find_element_by_link_text("IPO・PO").click()
        try:
            a.driver.find_element_by_xpath("//img[@alt='新規上場株式ブックビルディング / 購入意思表示']").click()
        except:
            a.driver.quit()
        try:
            a.driver.find_element_by_xpath("//img[@alt='申込']").click()
        except:
            break
        a.driver.find_element_by_name("suryo").send_keys("30000")
        a.driver.find_element_by_id("strPriceRadio").click()
        a.driver.find_element_by_id("ipoRadio1").click()
        a.driver.find_element_by_name("tr_pass").send_keys(a.decrypt(a.args.password2))
        a.driver.find_element_by_name("order_kakunin").click()
        a.screenshot()
        a.driver.find_element_by_name("order_btn").click()
        a.screenshot()
        print("SBI証券IPO("+str(i)+")に申し込みました", file=sys.stderr)
        
    a.driver.quit()
except:
    a.exit_on_err()
