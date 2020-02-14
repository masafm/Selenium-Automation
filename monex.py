#!/usr/bin/python3
from common import IPO
import sys

ipo = IPO('monex')

try:
    ipo.driver.get('https://www.monex.co.jp/')
    ipo.driver.find_element_by_id("loginid").send_keys(ipo.args.user)
    ipo.driver.find_element_by_id("passwd").send_keys(ipo.decrypt(ipo.args.password))
    ipo.driver.find_element_by_xpath("//button[contains(.,'ログイン')]").click()
    
    for i in range(5):
        ipo.driver.find_element_by_link_text("株式取引").click()
        ipo.driver.find_element_by_link_text("新規公開株(IPO)").click()
        ipo.driver.find_element_by_link_text("銘柄一覧（ブックビルディング参加）").click()
        ipo.driver.find_element_by_xpath("(//table[@class='table-block type-bg-02 type-border-01'])[1]").click()

        try:
            ipo.driver.find_element_by_xpath("(//table[@class='table-block type-bg-02 type-border-01'])[1]//a[contains(text(),'需要申告')]").click()
        except:
            break
        try:
            ipo.driver.implicitly_wait(3)
            pdf = ipo.driver.find_elements_by_xpath("//td[@class='al-l']/a")
            for p in pdf:
                p.click()
                handle_array = ipo.driver.window_handles
                ipo.driver.switch_to.window(handle_array[-1])
                ipo.driver.switch_to.frame(ipo.driver.find_element_by_xpath("//frame[@name='CT']"))
                ipo.driver.find_element_by_xpath("//a[contains(text(), '確認しました')]").click()
                
            ipo.driver.find_element_by_xpath("//input[@value='全て閲覧済み']").click()
        except:
            pass
        
        ipo.driver.find_element_by_id("orderNominal").send_keys("100")
        ipo.driver.find_element_by_id("n1").click()
        ipo.driver.find_element_by_xpath("//input[@value='次へ（申告内容確認）']").click()
        ipo.driver.find_element_by_id("idPinNo").send_keys(ipo.decrypt(ipo.args.password2))
        ipo.screenshot()
        ipo.driver.find_element_by_xpath("//input[@value='実行する']").click()
        ipo.screenshot()    
        print("マネックス証券IPO("+str(i)+")に申し込みました", file=sys.stderr)
    
    ipo.driver.quit()
except:
    ipo.exit_on_err()
