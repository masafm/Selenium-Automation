#!/usr/bin/env python3
from common import Automation
import sys
import time

a = Automation('monex')

try:
    a.driver.get('https://www.monex.co.jp/')
    a.driver.find_element_by_id("loginid").send_keys(a.args.user)
    a.driver.find_element_by_id("passwd").send_keys(a.decrypt(a.args.password))
    a.driver.find_element_by_xpath("//button[contains(.,'ログイン')]").click()
    
    for i in range(5):
        a.driver.find_element_by_link_text("株式取引").click()
        a.driver.find_element_by_link_text("新規公開株(IPO)").click()
        a.driver.find_element_by_link_text("銘柄一覧（ブックビルディング参加）").click()
        a.driver.find_element_by_xpath("(//table[@class='table-block type-bg-02 type-border-01'])[1]").click()

        try:
            a.driver.find_element_by_xpath("(//table[@class='table-block type-bg-02 type-border-01'])[1]//a[contains(text(),'需要申告')]").click()
        except:
            break
        try:
            pdf = a.driver.find_elements_by_xpath("//td[@class='al-l']/a")
            for p in pdf:
                p.click()
                handle_array = a.driver.window_handles
                a.driver.switch_to.window(handle_array[-1])
                a.driver.switch_to.frame(a.driver.find_element_by_xpath("//frame[@name='CT']"))
                time.sleep(3)
                a.driver.find_element_by_xpath("//a[contains(text(), '確認しました')]").click()
        except:
            pass
        try:                
            handle_array = a.driver.window_handles
            a.driver.switch_to.window(handle_array[0])
            time.sleep(3)
            a.driver.find_element_by_xpath("//input[@value='全て閲覧済み']").click()
        except:
            pass
        
        a.driver.find_element_by_id("orderNominal").send_keys("100")
        a.driver.find_element_by_id("n1").click()
        a.driver.find_element_by_xpath("//input[@value='次へ（申告内容確認）']").click()
        a.driver.find_element_by_id("idPinNo").send_keys(a.decrypt(a.args.password2))
        a.screenshot()
        a.driver.find_element_by_xpath("//input[@value='実行する']").click()
        a.screenshot()
        print("マネックス証券IPO("+str(i)+")に申し込みました", file=sys.stderr)
    
    a.driver.quit()
except:
    a.exit_on_err()
