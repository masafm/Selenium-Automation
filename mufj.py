#!/usr/bin/env python3
from common import Automation
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import sys
import time

a = Automation('mufj')

def click(target):
    actions = ActionChains(a.driver)
    actions.move_to_element(target)
    actions.perform()
    a.driver.execute_script("window.scrollBy(0, 100);")
    target.click()    

try:
    a.driver.get('https://online.sc.mufg.jp/its/dfw/UTBSITS/user_p/Login')
    a.driver.find_element_by_id("accountNumber").send_keys(a.args.user)
    a.driver.find_element_by_id("password").send_keys(a.decrypt(a.args.password))
    a.driver.find_element_by_xpath("//button[@title='ログイン']").click()
    try:
        a.driver.find_element_by_xpath("//button[@title='もう一度、ログインする']").click()
    except:
        pass
    for i in range(5):
        try:
            a.driver.find_element_by_xpath("//button[@title='次へ']").click()
            continue
        except:
            break

    click(a.driver.find_element_by_xpath("//a/span[.='取引・照会']"))
    click(a.driver.find_element_by_link_text("申込"))
    ipo_list = []
    try:
        ipo_list = a.driver.find_elements_by_xpath("//a[@title='申込']")
    except:
        pass

    length = 20
    if len(ipo_list) < 20:
        length = len(ipo_list)
        
    for i in range(length):
        a.driver.find_element_by_xpath("//a/span[.='取引・照会']").click()
        a.driver.find_element_by_link_text("申込").click()
        click(a.driver.find_elements_by_xpath("//a[@title='申込']")[i])
        click(a.driver.find_element_by_xpath("//label[contains(.,'はい')]"))
        click(a.driver.find_element_by_xpath("//button[@title='同意して次に進む']"))
        a.driver.find_element_by_name("prm_unit").send_keys('100')
        click(a.driver.find_element_by_xpath("//button[@title='申込内容を確認する']"))
        try:
            a.driver.find_element_by_name("prm_password").send_keys(a.decrypt(a.args.password2))
        except:
            a.driver.find_element_by_xpath("//a[@title='トップに戻る']").click()
            continue
            
        a.screenshot()
        a.driver.find_element_by_xpath("//button[@title='申込を送信する']").click()
        a.screenshot()    
        print("三菱UFJモルガン・スタンレー証券IPO("+str(i)+")に申し込みました", file=sys.stderr)
    
    a.driver.quit()
except:
    a.exit_on_err()
