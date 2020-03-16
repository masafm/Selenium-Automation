#!/usr/bin/python3
from common import IPO
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import sys
import time

ipo = IPO('mufj')

def click(target):
    actions = ActionChains(ipo.driver)
    actions.move_to_element(target)
    actions.perform()
    ipo.driver.execute_script("window.scrollBy(0, 100);")
    target.click()    

try:
    ipo.driver.get('https://online.sc.mufg.jp/its/dfw/UTBSITS/user_p/Login')
    ipo.driver.find_element_by_id("accountNumber").send_keys(ipo.args.user)
    ipo.driver.find_element_by_id("password").send_keys(ipo.decrypt(ipo.args.password))
    ipo.driver.find_element_by_xpath("//button[@title='ログイン']").click()
    try:
        ipo.driver.find_element_by_xpath("//button[@title='もう一度、ログインする']").click()
    except:
        pass
    try:
        ipo.driver.find_element_by_xpath("//button[@title='次へ']").click()
    except:
        pass

    ipo.driver.find_element_by_xpath("//a/span[.='取引・照会']").click()
    ipo.driver.find_element_by_link_text("申込").click()
    ipo_list = []
    try:
        ipo_list = ipo.driver.find_elements_by_xpath("//a[@title='申込']")
    except:
        pass

    length = 20
    if len(ipo_list) < 20:
        length = len(ipo_list)
        
    for i in range(length):
        ipo.driver.find_element_by_xpath("//a/span[.='取引・照会']").click()
        ipo.driver.find_element_by_link_text("申込").click()
        click(ipo.driver.find_elements_by_xpath("//a[@title='申込']")[i])
        click(ipo.driver.find_element_by_xpath("//label[contains(.,'はい')]"))
        click(ipo.driver.find_element_by_xpath("//button[@title='同意して次に進む']"))
        ipo.driver.find_element_by_name("prm_unit").send_keys('100')
        click(ipo.driver.find_element_by_xpath("//button[@title='申込内容を確認する']"))
        try:
            ipo.driver.find_element_by_name("prm_password").send_keys(ipo.decrypt(ipo.args.password2))
        except:
            ipo.driver.find_element_by_xpath("//a[@title='トップに戻る']").click()
            continue
            
        ipo.screenshot()
        ipo.driver.find_element_by_xpath("//button[@title='申込を送信する']").click()
        ipo.screenshot()    
        print("三菱UFJモルガン・スタンレー証券IPO("+str(i)+")に申し込みました", file=sys.stderr)
    
    ipo.driver.quit()
except:
    ipo.exit_on_err()
