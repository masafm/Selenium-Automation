#!/usr/bin/python3
from common import IPO
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import sys
import time

ipo = IPO('rakuten_keirin')

def click(target):
    actions = ActionChains(ipo.driver)
    actions.move_to_element(target)
    actions.perform()
    ipo.driver.execute_script("window.scrollBy(0, 100);")
    target.click()
    
try:
    ipo.driver.get('http://keirin.jp/pc/top')
    ipo.driver.find_element_by_id("trtxtBallotID").send_keys(ipo.args.user)
    ipo.driver.find_element_by_id("trtxtBallotPW").send_keys(ipo.decrypt(ipo.args.password))
    ipo.driver.find_element_by_xpath("//input[@value='ログイン']").click()
    time.sleep(1)
    click(ipo.driver.find_element_by_xpath("//button[text()='精　算']"))
    time.sleep(1)
    ipo.driver.find_element_by_id("UNQ_orbutton_36").click()
    ipo.driver.find_element_by_name("UNQ_orexpandText_11").send_keys(ipo.decrypt(ipo.args.password2))
    ipo.driver.find_element_by_id("UNQ_orbutton_18").click()
    time.sleep(5)
except:
    pass

try:
    ipo.driver.get('http://keirin.jp/pc/top')
    ipo.driver.find_element_by_id("trtxtBallotID").send_keys(ipo.args.user)
    ipo.driver.find_element_by_id("trtxtBallotPW").send_keys(ipo.decrypt(ipo.args.password))
    ipo.driver.find_element_by_xpath("//input[@value='ログイン']").click()
    time.sleep(1)
    click(ipo.driver.find_element_by_xpath("//button[text()='入　金']"))
    ipo.driver.find_element_by_id("UNQ_orexpandText_12").send_keys('1')
    time.sleep(1)
    ipo.driver.find_element_by_id("UNQ_orbutton_36").click()
    ipo.driver.find_element_by_name("UNQ_pfInputText_14").send_keys(ipo.decrypt(ipo.args.password2))
    ipo.driver.find_element_by_id("UNQ_orbutton_18").click()
    time.sleep(5)
except:
    pass

ipo.driver.quit()
