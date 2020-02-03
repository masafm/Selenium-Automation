#!/usr/bin/python3
from common import IPO
import sys

ipo = IPO('nomura')

try:
    ipo.driver.get('https://hometrade.nomura.co.jp/web/rmfIndexWebAction.do?loginType=1')
    ipo.driver.find_element_by_id("text01").send_keys(ipo.args.user)
    ipo.driver.find_element_by_id("passwd1").send_keys(ipo.decrypt(ipo.args.password))
    ipo.driver.find_element_by_name("buttonLogin").click()
    try:
        ipo.driver.implicitly_wait(3)
        ipo.driver.find_element_by_name("buttonTop").click()
        ipo.driver.implicitly_wait(30)
    except:
        pass
    ipo.driver.find_element_by_link_text("取引").click()
    ipo.driver.find_element_by_link_text("IPO/PO").click()
    ipo.driver.implicitly_wait(1)
    try:
        ipo.driver.find_element_by_xpath("//p[contains(.,'対象明細はありません。')]").click()
    except:
        ipo.driver.implicitly_wait(30)
        print("野村證券IPOがある場合の処理", file=sys.stderr)
    ipo.driver.quit()
except:
    ipo.exit_on_err()
