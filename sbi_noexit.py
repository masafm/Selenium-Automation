#!/usr/bin/env python3
from common import Automation
import sys
import time

a = Automation('sbi')

try:
    a.driver.get('https://www.sbisec.co.jp/')
    a.driver.find_element_by_name("user_id").send_keys(a.args.user)
    a.driver.find_element_by_name("user_password").send_keys(a.decrypt(a.args.password))
    a.driver.find_element_by_name("ACT_login").click()
    
except:
    a.exit_on_err()
