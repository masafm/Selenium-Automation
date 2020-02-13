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
        # 最初のお知らせスキップ
        ipo.driver.implicitly_wait(3)
        ipo.driver.find_element_by_name("buttonTop").click()
        ipo.driver.implicitly_wait(30)
    except:
        pass
    
    for i in range(5):
        ipo.driver.find_element_by_link_text("取引").click()
        ipo.driver.find_element_by_link_text("IPO/PO").click()
        try:
            ipo.driver.find_element_by_xpath("//a[contains(text(), '抽選申込へ')]").click();
        except:
            break
        checkboxes = ipo.driver.find_elements_by_xpath("//input[@type='checkbox']")
        for c in checkboxes:
            c.click()
        ipo.driver.find_element_by_xpath("//button[@name='buttonAgree']").click()
        ipo.driver.find_element_by_class_name("apl-js-cmspsp").click()
        ipo.driver.find_element_by_xpath("//button[@name='buttonAgree']").click()
        ipo.driver.find_element_by_xpath("//button[@name='buttonConfirm']").click()
        ipo.driver.find_element_by_name("trhkPswd").send_keys(ipo.decrypt(ipo.args.password2))
        ipo.screenshot()
        ipo.driver.find_element_by_xpath("//button[@name='buttonAccept']").click()
        ipo.screenshot()
        print("野村証券IPO("+str(i)+")に申し込みました", file=sys.stderr)
        
    ipo.driver.quit()
except:
    ipo.exit_on_err()
