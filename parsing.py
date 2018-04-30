#coding: utf-8

from connect import driver
from bs4 import BeautifulSoup

#날짜 파싱
def dateparsing(startdate,enddate):
    
    f = open("E:/eclipse/workspace/nfdscrawling/최종크롤링(201405).xls", 'a')
    f.write(startdate)
    f.write(';')
    f.write(enddate)
    f.write(';')
    f.write('\n')
    
#시,구 파싱    
def cityguparsing(cityname, guname):
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find('table', class_="default")
    tbody = table.tbody
    firstbody = str(tbody.get_text())

    f = open("E:/eclipse/workspace/nfdscrawling/최종크롤링(201405).xls", 'a')
    f.write(';;' + '삭제탭' +';')
    f.write(cityname)
    f.write(';')
    f.write(guname)

    tmp = firstbody.replace('\n', ';')
    cigu = str('\n;;' + '삭제탭' +';'+ cityname +';' + guname + ';')
    tmp2 = tmp.replace(';;;', cigu)
    f.write(tmp2)
    f.write('\n')
