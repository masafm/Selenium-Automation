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
    ipo.driver.find_element_by_xpath("//span[contains(.,'取引')]").click()
    ipo.driver.find_element_by_link_text("IPO/PO注文").click()
    ipo.driver.implicitly_wait(1)
    try:
        ipo.driver.find_element_by_xpath("//p[contains(.,'現在取扱中の銘柄はありません。')]").click()
    except:
        ipo.driver.implicitly_wait(30)
        print("岡三オンライン証券IPOがある場合の処理", file=sys.stderr)
    ipo.driver.quit()
except:
    ipo.exit_on_err()
