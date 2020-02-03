#!/usr/bin/python3
from common import IPO
import sys

ipo = IPO('daiwa')

try:
    ipo.driver.get('https://www.daiwa.jp/')
    ipo.driver.find_element_by_link_text("ログイン").click()
    ipo.driver.find_element_by_id("putbox1").send_keys(ipo.args.store)
    ipo.driver.find_element_by_id("putbox2").send_keys(ipo.args.user)
    ipo.driver.find_element_by_id("putbox3").send_keys(ipo.decrypt(ipo.args.password))
    ipo.driver.find_element_by_xpath("//input[@value='ログイン']").click()
    
    for i in range(5):
        ipo.driver.find_element_by_link_text("新規公開/公募売出").click()
        ipo.driver.find_element_by_link_text("新規公開株式").click()
        ipo.driver.find_element_by_link_text("抽選参加申込").click()
        try:
            ipo.driver.find_element_by_link_text("はい").click()
            ipo.driver.find_element_by_name("RADIO_DATA").click()
        except:
            break
        ipo.driver.find_element_by_name("確認へ").click()
        ipo.driver.find_element_by_xpath("//input[6]").click()
        ipo.driver.find_element_by_name("ANSHO_NO").send_keys(ipo.decrypt(ipo.args.password2))
        ipo.screenshot()
        ipo.driver.find_element_by_name("MOUSIKOMI").click()
        ipo.screenshot()
        print("大和証券IPO("+str(i)+")に申し込みました", file=sys.stderr)
        
    ipo.driver.quit()
    
except:
    ipo.exit_on_err()
