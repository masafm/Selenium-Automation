#!/usr/bin/python3
# pip3 install --user google-api-python-client oauth2client
from selenium import webdriver
from common import Automation
from datetime import datetime as dt
import sys
import os
import time

from apiclient import discovery
import oauth2client
from oauth2client import file
from oauth2client import tools
import httplib2
import argparse
import csv

RANGE_NAME = 'A1'
MAJOR_DIMENSION = 'ROWS'

CLIENT_SECRET_FILE = os.environ['HOME']+'/client_secret.json'
CREDENTIAL_FILE = os.environ['HOME']+'/credential.json'
APPLICATION_NAME = 'SBI USD Appender'

def c(col):
    index = {'A':'1','B':'2','C':'3','D':'4','E':'5','F':'6','G':'7','H':'8','I':'9','J':'10','K':'11','L':'12','M':'13','N':'14','O':'15','P':'16','Q':'17','R':'18','S':'19','T':'20','U':'21','V':'22','W':'23','X':'24','Y':'25','Z':'26'}
    return 'INDIRECT(ADDRESS(ROW(),'+index[col]+'))'

a = Automation('sbi_usd')

try:
    a.driver.get('https://www.sbisec.co.jp/')
    time.sleep(1)
    a.driver.find_element_by_name("user_id").send_keys(a.args.user)
    time.sleep(1)
    a.driver.find_element_by_name("user_password").send_keys(a.decrypt(a.args.password))
    time.sleep(1)
    a.driver.find_element_by_name("ACT_login").click()
    time.sleep(3)
    
    a.driver.find_element_by_xpath("//img[@alt='口座管理']").click()
    time.sleep(3)
    a.driver.find_element_by_xpath("//div[@id='navi02P']//a[.='口座（外貨建）']").click()
    usd = a.driver.find_element_by_xpath("//tr[@id='summary_USD']/td[3]//tr[1]/td[2]").text.replace(',','')
    jpy = a.driver.find_element_by_xpath("//tr[@id='summary_USD']/td[3]//tr[2]/td[2]").text.replace(',','')
    date = dt.now().strftime('%Y/%m/%d')

    store = oauth2client.file.Storage(CREDENTIAL_FILE)
    credentials = store.get()
    if not credentials or credentials.invalid:
        SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
        flow = oauth2client.client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        args = '--auth_host_name localhost --logging_level INFO --noauth_local_webserver'
        flags = argparse.ArgumentParser(parents=[oauth2client.tools.argparser]).parse_args(args.split())
        credentials = oauth2client.tools.run_flow(flow, store, flags)

    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?' 'version=v4')
    service = discovery.build('sheets', 'v4', http=http, discoveryServiceUrl=discoveryUrl)
    resource = service.spreadsheets().values()

    body = {
        "range": RANGE_NAME,
        "majorDimension": MAJOR_DIMENSION,
        "values": list(csv.reader([date+',損益確認,,,,,'+
                                   '"=SUM($E$1:'+c('E')+')-SUM($C$1:'+c('C')+')",'+
                                   jpy+','+
                                   '"=SUM($F$2:'+c('F')+')-SUM($D$2:'+c('D')+')",'+
                                   usd+','+
                                   '"=IF('+c('H')+','+c('H')+'-'+c('G')+', """")",'+
                                   '"=('+c('G')+'/'+c('N')+'-'+c('G')+'/'+c('M')+')*'+c('M')+'",'+
                                   '"='+c('H')+'/'+c('J')+'",'+
                                   '"='+c('G')+'/(SUM($F$1:'+c('F')+')-SUM($D$1:'+c('D')+'))"']))
    }
    resource.append(spreadsheetId=a.args.spreadsheet, range=RANGE_NAME,
                    valueInputOption='USER_ENTERED', body=body).execute()

    a.driver.quit()
except:
    a.exit_on_err()
