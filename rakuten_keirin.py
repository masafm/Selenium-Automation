#!/usr/bin/python3
from common import Automation
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import sys
import time

a = Automation('rakuten_keirin')

def click(target):
    actions = ActionChains(a.driver)
    actions.move_to_element(target)
    actions.perform()
    a.driver.execute_script("window.scrollBy(0, 100);")
    target.click()
    
try:
    a.driver.get('http://keirin.jp/pc/top')
    a.driver.find_element_by_id("trtxtBallotID").send_keys(a.args.user)
    a.driver.find_element_by_id("trtxtBallotPW").send_keys(a.decrypt(a.args.password))
    a.driver.find_element_by_xpath("//input[@value='ログイン']").click()
    time.sleep(1)
    click(a.driver.find_element_by_xpath("//button[text()='精　算']"))
    time.sleep(1)
    a.driver.find_element_by_id("UNQ_orbutton_36").click()
    a.driver.find_element_by_name("UNQ_orexpandText_11").send_keys(a.decrypt(a.args.password2))
    a.driver.find_element_by_id("UNQ_orbutton_18").click()
    time.sleep(5)
except:
    pass

try:
    a.driver.get('http://keirin.jp/pc/top')
    a.driver.find_element_by_id("trtxtBallotID").send_keys(a.args.user)
    a.driver.find_element_by_id("trtxtBallotPW").send_keys(a.decrypt(a.args.password))
    a.driver.find_element_by_xpath("//input[@value='ログイン']").click()
    time.sleep(1)
    click(a.driver.find_element_by_xpath("//button[text()='入　金']"))
    a.driver.find_element_by_id("UNQ_orexpandText_12").send_keys('1')
    time.sleep(1)
    a.driver.find_element_by_id("UNQ_orbutton_36").click()
    a.driver.find_element_by_name("UNQ_pfInputText_14").send_keys(a.decrypt(a.args.password2))
    a.driver.find_element_by_id("UNQ_orbutton_18").click()
    time.sleep(5)
except:
    pass

a.driver.quit()
