#!/usr/bin/env python3
from common import Automation
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import sys
import time

a = Automation('rakuten_keirin_out')

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

    a.driver.quit()
except:
    a.exit_on_err()
