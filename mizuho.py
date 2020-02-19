#!/usr/bin/python3
from common import IPO
import sys

ipo = IPO('mizuho')

try:
    ipo.driver.get('https://netclub.mizuho-sc.com/mnc/login?rt_bn=sc_top_hd_login')
    ipo.driver.find_element_by_id("IDInputKB").send_keys(ipo.args.user)
    ipo.driver.find_element_by_id("PWInputKB").send_keys(ipo.decrypt(ipo.args.password))
    ipo.driver.find_element_by_name("send").click()

    for i in range(5):
        ipo.driver.find_element_by_link_text("お取引").click()
        ipo.driver.find_element_by_link_text("IPO/PO(募集・売出し銘柄)").click()
        ipo.driver.find_element_by_xpath("(//table[@class='tblMod02 mgt10t'])[1]").click()
        try:
            ipo.driver.find_element_by_xpath("(//table[@class='tblMod02 mgt10t'])[1]//a[contains(text(),'申込')]").click()
        except:
            break
        ipo.driver.find_element_by_xpath("//input[@value='次へ']").click()
        ipo.driver.find_element_by_xpath("//input[@value='同意する']").click()
        try:
            ipo.driver.find_element_by_xpath("//input[@value='電子交付を承認する']").click()
            pdf = ipo.driver.find_elements_by_xpath("//a[contains(@href,'.pdf')]")
            for p in pdf:
                p.click()
            ipo.driver.find_element_by_xpath("//input[@value='内容を理解した']").click()
        except:
            pass
        ipo.driver.find_element_by_name("kabuSuFeedbackPanelParent:mousikomiKabusuu:base:_value").send_keys('1')
        ipo.driver.find_element_by_name("kakakuFeedbackPanelParent:nedanRadioChoice").click()
        ipo.driver.find_element_by_xpath("//input[@value='申込確認画面へ']").click()
        ipo.driver.implicitly_wait(5)
        try:
            ipo.driver.find_element_by_name("ansyouBangouFeedbackPanelParent:ansyouBangou").send_keys(ipo.decrypt(ipo.args.password2))
        except:
            ipo.driver.implicitly_wait(30)
            ipo.driver.find_element_by_name("kabuSuFeedbackPanelParent:mousikomiKabusuu:base:_value").clear()
            ipo.driver.find_element_by_name("kabuSuFeedbackPanelParent:mousikomiKabusuu:base:_value").send_keys('100')
            ipo.driver.find_element_by_name("kakakuFeedbackPanelParent:nedanRadioChoice").click()
            ipo.driver.find_element_by_xpath("//input[@value='申込確認画面へ']").click()
            ipo.driver.find_element_by_name("ansyouBangouFeedbackPanelParent:ansyouBangou").send_keys(ipo.decrypt(ipo.args.password2))
        ipo.driver.implicitly_wait(30)
        ipo.screenshot()
        ipo.driver.find_element_by_xpath("//input[@value='説明を理解し抽選参加する']").click()
        ipo.screenshot()
        print("みずほ証券IPO("+str(i)+")に申し込みました", file=sys.stderr)
        
    ipo.driver.quit()
except:
    ipo.exit_on_err()
