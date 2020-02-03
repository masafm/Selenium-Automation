#!/usr/bin/python3
from common import IPO
import sys

ipo = IPO('rakuten')

try:
    ipo.driver.get('https://www.rakuten-sec.co.jp/')
    ipo.driver.find_element_by_id("form-login-id").send_keys(ipo.args.user)
    ipo.driver.find_element_by_id("form-login-pass").send_keys(ipo.decrypt(ipo.args.password))
    ipo.driver.find_element_by_xpath("//button[contains(.,' ログイン')]").click()

    ipo.driver.find_element_by_link_text("国内株式").click()
    ipo.driver.find_element_by_link_text("IPO（PO）に参加する").click()
    ipo.driver.implicitly_wait(1)
    try:
        ipo.driver.find_element_by_xpath("//span[contains(.,'該当する情報はありません。')]").click()
    except:
        ipo.driver.implicitly_wait(30)
        #print("楽天證券IPOがある場合の処理", file=sys.stderr)
    ipo.driver.quit()
except:
    ipo.exit_on_err()
