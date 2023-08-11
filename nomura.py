#!/usr/bin/env python3
from common import Automation
import sys

a = Automation('nomura')

try:
    a.driver.get('https://hometrade.nomura.co.jp/web/rmfIndexWebAction.do?loginType=1')
    a.driver.find_element_by_id("text01").send_keys(a.args.user)
    a.driver.find_element_by_id("passwd1").send_keys(a.decrypt(a.args.password))
    a.driver.find_element_by_name("buttonLogin").click()
    try:
        # 最初のお知らせスキップ
        a.driver.find_element_by_name("buttonTop").click()
    except:
        pass
    
    for i in range(5):
        a.driver.find_element_by_link_text("取引").click()
        a.driver.find_element_by_link_text("IPO/PO").click()
        try:
            a.driver.find_element_by_xpath("//a[contains(text(), '抽選申込へ')]").click();
        except:
            break
        checkboxes = a.driver.find_elements_by_xpath("//input[@type='checkbox']")
        for c in checkboxes:
            c.click()
        a.driver.find_element_by_xpath("//button[@name='buttonAgree']").click()
        a.driver.find_element_by_class_name("apl-js-cmspsp").click()
        a.driver.find_element_by_xpath("//button[@name='buttonAgree']").click()
        a.driver.find_element_by_xpath("//button[@name='buttonConfirm']").click()
        a.driver.find_element_by_name("trhkPswd").send_keys(a.decrypt(a.args.password2))
        a.screenshot()
        a.driver.find_element_by_xpath("//button[@name='buttonAccept']").click()
        a.screenshot()
        print("野村証券IPO("+str(i)+")に申し込みました", file=sys.stderr)
        
    a.driver.quit()
except:
    a.exit_on_err()
