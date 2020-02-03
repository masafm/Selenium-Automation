#!/usr/bin/python3
from common import IPO
import sys

ipo = IPO('sbi')

try:
    ipo.driver.get('https://www.sbisec.co.jp/')
    ipo.driver.find_element_by_name("user_id").send_keys(ipo.args.user)
    ipo.driver.find_element_by_name("user_password").send_keys(ipo.decrypt(ipo.args.password))
    ipo.driver.find_element_by_name("ACT_login").click()
    
    for i in range(5):
        ipo.driver.find_element_by_xpath("//img[@alt='ホーム']").click()
        ipo.driver.find_element_by_xpath("//img[@alt='国内株式']").click()
        ipo.driver.find_element_by_link_text("IPO・PO").click()
        ipo.driver.find_element_by_xpath("//img[@alt='新規上場株式ブックビルディング / 購入意思表示']").click()
        try:
            ipo.driver.find_element_by_xpath("//img[@alt='申込']").click()
        except:
            break
        ipo.driver.find_element_by_name("suryo").send_keys("100000")
        ipo.driver.find_element_by_id("strPriceRadio").click()
        ipo.driver.find_element_by_id("ipoRadio1").click()
        ipo.driver.find_element_by_name("tr_pass").send_keys(ipo.decrypt(ipo.args.password2))
        ipo.driver.find_element_by_name("order_kakunin").click()
        ipo.screenshot()
        ipo.driver.find_element_by_name("order_btn").click()
        ipo.screenshot()
        print("SBI証券IPO("+str(i)+")に申し込みました", file=sys.stderr)
        
    ipo.driver.quit()
except:
    ipo.exit_on_err()
