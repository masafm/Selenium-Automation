#!/usr/bin/python3
from common import Automation
import sys
import time

a = Automation('mizuho')

try:
    a.driver.get('https://netclub.mizuho-sc.com/mnc/login?rt_bn=sc_top_hd_login')
    a.driver.find_element_by_id("IDInputKB").send_keys(a.args.user)
    a.driver.find_element_by_id("PWInputKB").send_keys(a.decrypt(a.args.password))
    a.driver.find_element_by_name("send").click()

    for i in range(5):
        a.driver.find_element_by_link_text("お取引").click()
        a.driver.find_element_by_link_text("IPO/PO(募集・売出し銘柄)").click()
        try:
            a.driver.find_element_by_xpath("(//table[@class='tblMod02 mgt10t'])[1]").click()
            a.driver.find_element_by_xpath("(//table[@class='tblMod02 mgt10t'])[1]//a[contains(text(),'申込')]").click()
        except:
            break
        a.driver.find_element_by_xpath("//input[@value='次へ']").click()
        a.driver.find_element_by_xpath("//input[@value='同意する']").click()
        try:
            a.driver.find_element_by_xpath("//input[@value='電子交付を承認する']").click()
        except:
            pass
        try:
            a.driver.find_element_by_xpath("//input[@id='doui']").click()
            time.sleep(2)
            a.driver.find_element_by_xpath("//input[@value='目論見書を閲覧する']").click()
        except:
            pass
        try:
            pdf = a.driver.find_elements_by_xpath("//a[contains(@href,'.pdf')]")
            for p in pdf:
                p.click()
            time.sleep(30)
            a.driver.find_element_by_xpath("//input[@value='内容を理解した']").click()
        except:
            pass

        kabu_su=['1','100','200']
        for k in kabu_su:
            a.driver.find_element_by_name("kabuSuFeedbackPanelParent:mousikomiKabusuu:base:_value").clear()
            a.driver.find_element_by_name("kabuSuFeedbackPanelParent:mousikomiKabusuu:base:_value").send_keys(k)
            a.driver.find_element_by_name("kakakuFeedbackPanelParent:nedanRadioChoice").click()
            a.driver.find_element_by_xpath("//input[@value='申込確認画面へ']").click()
            try:
                a.driver.find_element_by_name("ansyouBangouFeedbackPanelParent:ansyouBangou").send_keys(a.decrypt(a.args.password2))
            except:
                continue
            break
                
        a.screenshot()
        a.driver.find_element_by_xpath("//input[@value='説明を理解し抽選参加する']").click()
        a.screenshot()
        print("みずほ証券IPO("+str(i)+")に申し込みました", file=sys.stderr)
        
    a.driver.quit()
except:
    a.exit_on_err()
