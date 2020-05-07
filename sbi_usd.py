#!/usr/bin/python3
from common import Automation
from datetime import datetime as dt
import sys

a = Automation('sbi_usd')

try:
    a.driver.get('https://www.sbisec.co.jp/')
    a.driver.find_element_by_name("user_id").send_keys(a.args.user)
    a.driver.find_element_by_name("user_password").send_keys(a.decrypt(a.args.password))
    a.driver.find_element_by_name("ACT_login").click()
    
    a.driver.find_element_by_xpath("//img[@alt='口座管理']").click()
    a.driver.find_element_by_link_text("口座（外貨建）").click()
    usd = a.driver.find_element_by_xpath("//tr[@id='summary_USD']/td[3]//tr[1]/td[2]").text.replace(',','')
    jpy = a.driver.find_element_by_xpath("//tr[@id='summary_USD']/td[3]//tr[2]/td[2]").text.replace(',','')
    date = dt.now().strftime('%Y/%m/%d')
    with open('~/sbi_usd.csv', mode='a') as file:
        file.write(date+',損益確認,,,,,,'+jpy+','+usd+'\n')
    a.driver.quit()
except:
    a.exit_on_err()
