#!/usr/bin/env python3
from common import Automation
import sys

a = Automation('okasan')

try:
    a.driver.get('https://www.okasan-online.co.jp/login/jp/')
    a.driver.find_element_by_id("loginId").send_keys(a.args.user)
    a.driver.find_element_by_id("loginPass").send_keys(a.decrypt(a.args.password))
    a.driver.find_element_by_id("sougouSubmit").click()
    a.driver.find_element_by_name("buttonOK").click()

    for i in range(5):
        a.driver.find_element_by_xpath("//span[contains(.,'取引')]").click()
        a.driver.find_element_by_xpath("//a[@title='IPO/PO']").click()
        a.driver.find_element_by_xpath("//a[@title='IPO/PO注文']").click()
        try:
            a.driver.find_element_by_xpath("//div[@id='TrdStkIpoLst_ListIPO_block']//a[contains(text(),'抽選申込へ')]").click()
        except:
            break
        a.driver.find_element_by_name("buttonOK").click()
        a.driver.find_element_by_name("chusnMuskmSuryu").send_keys("100")
        a.driver.find_element_by_id("TrdStkIpoDofInputWlimit").click()
        a.driver.find_element_by_name("insiderKknnFlg").click()
        a.driver.find_element_by_name("buttonConfirm").click()
        a.driver.find_element_by_id("passwd1").send_keys(a.decrypt(a.args.password2))
        a.screenshot()
        a.driver.find_element_by_xpath("//input[@alt='抽選申込']").click()
        a.screenshot()
        print("岡三オンライン証券IPO("+str(i)+")に申し込みました", file=sys.stderr)
    
    a.driver.quit()
except:
    a.exit_on_err()
