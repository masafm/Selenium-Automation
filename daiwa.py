#!/usr/bin/env python3
from common import Automation
import sys

a = Automation('daiwa')

try:
    a.driver.get('https://www.daiwa.jp/')
    a.driver.find_element_by_link_text("ログイン").click()
    a.driver.find_element_by_id("putbox1").send_keys(a.args.store)
    a.driver.find_element_by_id("putbox2").send_keys(a.args.user)
    a.driver.find_element_by_id("putbox3").send_keys(a.decrypt(a.args.password))
    a.driver.find_element_by_xpath("//input[@value='ログイン']").click()
    
    for i in range(5):
        a.driver.find_element_by_link_text("新規公開/公募売出").click()
        a.driver.find_element_by_link_text("新規公開株式").click()
        a.driver.find_element_by_link_text("抽選参加申込").click()
        try:
            a.driver.find_element_by_link_text("はい").click()
            a.driver.find_element_by_name("RADIO_DATA").click()
        except:
            break
        a.driver.find_element_by_name("確認へ").click()
        a.driver.find_element_by_xpath("//input[6]").click()
        a.driver.find_element_by_name("ANSHO_NO").send_keys(a.decrypt(a.args.password2))
        a.screenshot()
        a.driver.find_element_by_name("MOUSIKOMI").click()
        a.screenshot()
        print("大和証券IPO("+str(i)+")に申し込みました", file=sys.stderr)
        
    a.driver.quit()
    
except:
    a.exit_on_err()
