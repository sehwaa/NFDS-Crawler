#coding: utf-8

from selenium import webdriver

#ChromeDriver로 접속, 자원 로딩시간 3초
driver = webdriver.Chrome('E:/chromedriver/chromedriver_win32/chromedriver')
driver.implicitly_wait(3)

#웹페이지 불러오기
driver.get('http://www.nfds.go.kr/fr_base_0001.jsf')