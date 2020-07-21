#!/usr/bin/python3
from selenium import webdriver
from common import Automation
from datetime import datetime as dt
import sys
import os
import time

a = Automation('sbi_usd')

try:
    a.driver.get('https://www.sbisec.co.jp/')
    a.driver.find_element_by_name("user_id").send_keys(a.args.user)
    a.driver.find_element_by_name("user_password").send_keys(a.decrypt(a.args.password))
    a.driver.find_element_by_name("ACT_login").click()
    
    link = a.driver.find_element_by_xpath("//img[@alt='口座管理']")
    action = webdriver.common.action_chains.ActionChains(a.driver)
    action.move_to_element_with_offset(link, 1, 1)
    action.click()
    action.perform()
    link = a.driver.find_element_by_xpath("//div[@id='navi02P']//a[.='口座（外貨建）']")
    action = webdriver.common.action_chains.ActionChains(a.driver)
    action.move_to_element_with_offset(link, 1, 1)
    action.click()
    action.perform()
    usd = a.driver.find_element_by_xpath("//tr[@id='summary_USD']/td[3]//tr[1]/td[2]").text.replace(',','')
    jpy = a.driver.find_element_by_xpath("//tr[@id='summary_USD']/td[3]//tr[2]/td[2]").text.replace(',','')
    date = dt.now().strftime('%Y/%m/%d')
    with open(os.environ['HOME']+'/sbi_usd.csv', mode='a') as file:
        file.write(date+',損益確認,,,,,,'+jpy+',,'+usd+'\n')
    a.driver.quit()
except:
    a.exit_on_err()
