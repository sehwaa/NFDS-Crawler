#coding: utf-8

from connect import driver

#시 설정
def setCity(cityvalue):   
    city = driver.find_element_by_xpath("//option[@value='" + str(cityvalue) + "']")
    city.click()
    
def setCityName(cityvalue):
    city = driver.find_element_by_xpath("//option[@value='" + str(cityvalue) + "']")
    cityname = city.text
    return cityname