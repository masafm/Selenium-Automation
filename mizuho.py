#!/usr/bin/python3
from common import IPO
import sys

ipo = IPO('mizuho')

try:
    ipo.driver.get('')
    ipo.driver.find_element_by_name("").send_keys(ipo.args.user)
    ipo.driver.find_element_by_name("").send_keys(ipo.decrypt(ipo.args.password))
    ipo.driver.find_element_by_name("").click()
    
    for i in range(5):
        ipo.driver.find_element_by_xpath("").click()
        ipo.driver.find_element_by_link_text("").click()
        try:
            ipo.driver.find_element_by_xpath("").click()
        except:
            break
        ipo.driver.find_element_by_name("").send_keys("")
        ipo.driver.find_element_by_id("").click()
        ipo.screenshot()
        ipo.driver.find_element_by_name("").click()
        ipo.screenshot()
        print("みずほ証券IPO("+str(i)+")に申し込みました", file=sys.stderr)
        
    ipo.driver.quit()
except:
    ipo.exit_on_err()
