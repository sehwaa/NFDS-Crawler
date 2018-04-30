#coding: utf-8
from connect import driver

#날짜 설정
def setDate(startdate, enddate):
    #시작 날짜 설정
    start = driver.find_element_by_name('txtSdate')
    start.clear()
    start.send_keys(startdate)
    
    #종료 날짜 설정
    end = driver.find_element_by_name('txtEdate')
    end.clear()
    end.send_keys(enddate)