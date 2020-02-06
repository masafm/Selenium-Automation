#!/usr/bin/python3
from common import IPO
import sys
from selenium.webdriver.common.keys import Keys

ipo = IPO('smbc_nikko')

try:
    ipo.driver.get('https://trade.smbcnikko.co.jp/Login/0/login/ipan_web/hyoji/')
    ipo.driver.find_element_by_id("padInput0").send_keys(ipo.args.store)
    ipo.driver.find_element_by_id("padInput1").send_keys(ipo.args.user)
    ipo.driver.find_element_by_id("padInput2").send_keys(ipo.decrypt(ipo.args.password))
    ipo.driver.find_element_by_name("logIn").click()
    
    ipo.driver.get('https://trade.smbcnikko.co.jp/MoneyManagement/9404K0821255/ez_ipo/meigara/ichiran')
    ipo_list = []
    try:
        ipo_list = ipo.driver.find_elements_by_xpath("//img[@alt='需要申告受付中']")
    except:
        pass

    ipo.driver.implicitly_wait(5)
    for i in range(len(ipo_list)):
        ipo.driver.get('https://trade.smbcnikko.co.jp/MoneyManagement/9404K0821255/ez_ipo/meigara/ichiran')
        ipo.driver.find_elements_by_xpath("//img[@alt='需要申告受付中']")[i].click()
        ipo.driver.find_element_by_id("mcChk").click()
        ipo.driver.find_element_by_xpath("//input[@alt='次へ']").click()
        try:
            ipo.driver.find_element_by_name("snkokSu").send_keys('1')
            ipo.driver.find_element_by_name("snkokKakaku").click()
            ipo.driver.find_element_by_name("snkokKakaku").send_keys(Keys.ARROW_DOWN)
            ipo.driver.find_element_by_name("snkokKakaku").send_keys(Keys.ENTER)
        except:
            continue

        ipo.driver.find_element_by_xpath("//input[@alt='申告内容確認']").click()
        ipo.screenshot()
        try:
            ipo.driver.find_element_by_xpath("//input[@alt='需要申告']").click()
        except:
            ipo.driver.find_element_by_name("snkokSu").clear()
            ipo.driver.find_element_by_name("snkokSu").send_keys('100')
            ipo.driver.find_element_by_name("実行").click()
            ipo.screenshot()
            ipo.driver.find_element_by_xpath("//input[@alt='需要申告']").click()
            
        ipo.screenshot()
        print("SMBC日興証券IPO("+str(i)+")に申し込みました", file=sys.stderr)

    ipo.driver.quit()
except:
    ipo.exit_on_err()
