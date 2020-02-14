#!/usr/bin/python3
from common import IPO
import sys

ipo = IPO('okasan')

try:
    ipo.driver.get('https://www.okasan-online.co.jp/login/jp/')
    ipo.driver.find_element_by_id("loginId").send_keys(ipo.args.user)
    ipo.driver.find_element_by_id("loginPass").send_keys(ipo.decrypt(ipo.args.password))
    ipo.driver.find_element_by_id("sougouSubmit").click()
    ipo.driver.find_element_by_name("buttonOK").click()

    for i in range(5):
        ipo.driver.find_element_by_xpath("//span[contains(.,'取引')]").click()
        ipo.driver.find_element_by_xpath("//a[@title='IPO/PO注文']").click()
        try:
            ipo.driver.find_element_by_xpath("//div[@id='TrdStkIpoLst_ListIPO_block']//a[contains(text(),'抽選申込へ')]").click()
        except:
            break
        ipo.driver.find_element_by_name("buttonOK").click()
        ipo.driver.find_element_by_name("chusnMuskmSuryu").send_keys("100")
        ipo.driver.find_element_by_id("TrdStkIpoDofInputWlimit").click()
        ipo.driver.find_element_by_name("insiderKknnFlg").click()
        ipo.driver.find_element_by_name("buttonConfirm").click()
        ipo.driver.find_element_by_id("passwd1").send_keys(ipo.decrypt(ipo.args.password2))
        ipo.screenshot()
        ipo.driver.find_element_by_xpath("//input[@alt='抽選申込']").click()
        ipo.screenshot()
        print("岡三オンライン証券IPO("+str(i)+")に申し込みました", file=sys.stderr)
    
    ipo.driver.quit()
except:
    ipo.exit_on_err()
