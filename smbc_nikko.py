#!/usr/bin/env python3
from common import Automation
import sys
from selenium.webdriver.common.keys import Keys

a = Automation('smbc_nikko')

try:
    a.driver.get('https://trade.smbcnikko.co.jp/Login/0/login/ipan_web/hyoji/')
    a.driver.find_element_by_id("padInput0").send_keys(a.args.store)
    a.driver.find_element_by_id("padInput1").send_keys(a.args.user)
    a.driver.find_element_by_id("padInput2").send_keys(a.decrypt(a.args.password))
    a.driver.find_element_by_name("logIn").click()
    
    a.driver.get('https://trade.smbcnikko.co.jp/MoneyManagement/9404K0821255/ez_ipo/meigara/ichiran')
    ipo_list = []
    try:
        ipo_list = a.driver.find_elements_by_xpath("//img[@alt='需要申告受付中']")
    except:
        pass

    for i in range(len(ipo_list)):
        a.driver.get('https://trade.smbcnikko.co.jp/MoneyManagement/9404K0821255/ez_ipo/meigara/ichiran')
        a.driver.find_elements_by_xpath("//img[@alt='需要申告受付中']")[i].click()
        a.driver.find_element_by_id("mcChk").click()
        a.driver.find_element_by_xpath("//input[@alt='次へ']").click()
        try:
            a.driver.find_element_by_name("snkokSu").send_keys('1')
            a.driver.find_element_by_name("snkokKakaku").click()
            a.driver.find_element_by_name("snkokKakaku").send_keys(Keys.ARROW_DOWN)
            a.driver.find_element_by_name("snkokKakaku").send_keys(Keys.ENTER)
        except:
            continue

        a.driver.find_element_by_xpath("//input[@alt='申告内容確認']").click()
        a.screenshot()
        try:
            a.driver.find_element_by_name("toriPasswd").send_keys(a.args.password2)
            a.driver.find_element_by_xpath("//input[@alt='需要申告']").click()
        except:
            a.driver.find_element_by_name("snkokSu").clear()
            a.driver.find_element_by_name("snkokSu").send_keys('100')
            a.driver.find_element_by_name("実行").click()
            a.screenshot()
            a.driver.find_element_by_name("toriPasswd").send_keys(a.args.password2)
            a.driver.find_element_by_xpath("//input[@alt='需要申告']").click()
            
        a.screenshot()
        print("SMBC日興証券IPO("+str(i)+")に申し込みました", file=sys.stderr)

    a.driver.quit()
except:
    a.exit_on_err()
