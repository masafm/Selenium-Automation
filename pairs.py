#!/usr/bin/env python3
from common import Automation
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import sys
import time
import re

a = Automation('pairs')

try:
    a.driver.get('https://pairs.lv/#/login')
    a.driver.find_element_by_xpath("//span[.='Facebookでログイン']").click()
    handle_array = a.driver.window_handles
    a.driver.switch_to.window(handle_array[-1])
    a.driver.find_element_by_id("email").send_keys(a.args.user)
    a.driver.find_element_by_id("pass").send_keys(a.decrypt(a.args.password))
    a.driver.find_element_by_id("loginbutton").click()
    time.sleep(3)
    a.driver.switch_to.window(handle_array[0])

    try:
        for i in range(4):
            a.driver.find_element_by_xpath("//*[.='無料で']").click()
            time.sleep(3)
    except:
        pass

    a.driver.get('https://pairs.lv/search')
    for i in range(1,500):
        if i%10 == 0:
            a.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            a.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
        a.driver.find_element_by_xpath("(//img[@class='lazy-img__zO0o_ css-u486sl-CircleImg lazy loaded'])["+str(i)+"]").click()
        
        like = a.driver.find_element_by_xpath("(//span[contains(., 'いいね！')])[1]/../span/span").text
        time.sleep(1)
        if like != '~5' and like != '500+' and int(like) > 70 and int(like) < 300:
            try:
                a.driver.find_element_by_xpath("//span[.='いいね！']").click()
                button = a.driver.find_element_by_xpath("(//div[@class='icon__2FIQ1 flex-row icon-large__1nEsE'])[3]")
                action = webdriver.common.action_chains.ActionChains(a.driver)
                action.move_to_element_with_offset(button, 20, 50)
                action.click()
                action.perform()
            except:
                a.driver.find_element_by_xpath("//div[@id='like_question_answer_modal']//img").click()
            time.sleep(1)
        try:
            a.driver.find_element_by_xpath("(//button[@class='css-1hgrnjs-pointerStyles-ButtonProtect'])[1]").click()
        except:
            pass

    a.driver.quit()
except:
    a.exit_on_err()
