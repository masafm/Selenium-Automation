#!/usr/bin/python3
import os
import sys
import argparse
from datetime import datetime as d
from selenium import webdriver
import xorcrypt as xc

class IPO:
    def __init__(self, name):
        self.name = name
        parser = argparse.ArgumentParser(description='')
        parser.add_argument('key')
        parser.add_argument('user')
        parser.add_argument('password')
        parser.add_argument('--store')
        parser.add_argument('--password2')
        self.args = parser.parse_args()
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def decrypt(self, value):
        return xc.decrypt(value, self.args.key)

    def screenshot(self):
        path = os.environ['HOME']+'/screenshot/'+self.name+'.'+d.today().strftime("%Y%m%d%H%M%S")+'.png'
        print(path, file=sys.stderr)
        self.driver.save_screenshot(path)

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
