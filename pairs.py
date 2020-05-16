#!/usr/bin/python3
from common import Automation
from selenium import webdriver
import sys
import time

a = Automation('pairs')

try:
    a.driver.get('https://pairs.lv/#/login')
    a.driver.find_element_by_class_name("login_button_a").click()
    handle_array = a.driver.window_handles
    a.driver.switch_to.window(handle_array[-1])
    a.driver.find_element_by_id("email").send_keys(a.args.user)
    a.driver.find_element_by_id("pass").send_keys(a.decrypt(a.args.password))
    a.driver.find_element_by_id("loginbutton").click()
    a.driver.switch_to.window(handle_array[0])
    try:
        a.driver.find_element_by_id("welcome_close_button").click()
    except:
        pass
    likes = a.driver.find_elements_by_xpath("//p[contains(text(), '今日のピックアップとは？')]//..//span[contains(text(), '無料でいいね!')]")
    time.sleep(10)
    for l in likes:
        action = webdriver.common.action_chains.ActionChains(a.driver)
        action.move_to_element_with_offset(l, 5, 5)
        action.click()
        try:
            action.perform()
        except:
            continue
        try:
            a.driver.find_element_by_xpath("//p[contains(text(), '「いいね！」を送りますか？')]//..//span[contains(text(), '無料で')]").click()
        except:
            a.driver.find_element_by_xpath("//div[@id='like_question_answer_modal']//img").click()
        time.sleep(3)

    a.driver.get('https://pairs.lv/')
    for i in range(1,10):
        a.driver.get('https://pairs.lv/#/search/grid/'+str(i))
        time.sleep(3)
        likes = a.driver.find_elements_by_xpath("//p[@class='user_like_count user_like_count_a']")
        buttons = a.driver.find_elements_by_xpath("//ul[@class='list_view_users']/..//span[.='いいね！']")
        for j in range(16):
            if int(likes[j].text.replace('+','')) > 90 and int(likes[j].text.replace('+','')) < 300:
                action = webdriver.common.action_chains.ActionChains(a.driver)
                action.move_to_element_with_offset(buttons[j], 5, 5)
                action.click()
                action.perform()
                try:
                    a.driver.find_element_by_xpath("//p[contains(text(), '「いいね！」を送りますか？')]/..//a[text()='いいね！']").click()
                except:
                    a.driver.find_element_by_xpath("//div[@id='like_question_answer_modal']//img").click()
                time.sleep(3)
    a.driver.quit()
except:
    a.exit_on_err()