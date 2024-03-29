#!/usr/bin/env python3
import os
import sys
import argparse
import time
from datetime import datetime as d
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import xorcrypt as xc

class Automation:
    def __init__(self, name):
        self.name = name
        parser = argparse.ArgumentParser(description='')
        parser.add_argument('key')
        parser.add_argument('user')
        parser.add_argument('password')
        parser.add_argument('--store')
        parser.add_argument('--password2')
        parser.add_argument('--spreadsheet')
        parser.add_argument('--proxy')
        self.args = parser.parse_args()
        options = Options()
        options.binary_location = "/usr/bin/chromium-browser"
        if self.args.proxy:
            options.add_argument('--proxy-server=http://%s' % self.args.proxy)
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

    def decrypt(self, value):
        return xc.decrypt(value, self.args.key)

    def screenshot(self):
        path = os.environ['HOME']+'/screenshot/'+self.name+'.'+d.today().strftime("%Y%m%d%H%M%S")+'.png'
        print(path, file=sys.stderr)
        self.driver.save_screenshot(path)
        time.sleep(1)

    def save_source(self):
        path = os.environ['HOME']+'/screenshot/'+self.name+'.'+d.today().strftime("%Y%m%d%H%M%S")+'.html'
        print(path, file=sys.stderr)
        file = open(path, mode='w')
        file.write(self.driver.page_source)
        file.close()
        
    def exit_on_err(self):
        print(sys.argv[0], file=sys.stderr)
        print(sys.exc_info(), file=sys.stderr)
        self.screenshot()
        self.save_source()
        self.driver.quit()
        sys.exit(1)
