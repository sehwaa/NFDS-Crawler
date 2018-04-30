#coding: utf-8

from connect import driver
from city import setCityName
from parsing import cityguparsing, dateparsing

#구 설정
def setGu(cityvalue):
    
    cityname = setCityName(cityvalue)
    
    if cityvalue == 11:
        for index in range(10,75):
            try:
                gu = driver.find_element_by_xpath("//option[@value='" + str(index*10) + "']")
                gu.click()
                guname = gu.text
                driver.find_element_by_xpath("//input[@type='image']").click()
                cityguparsing(cityname, guname)
            except:
                print(index)
    elif cityvalue == 26:
        for index in range(10,54):
            try:
                gu = driver.find_element_by_xpath("//option[@value='" + str(index*10) + "']")
                gu.click()
                guname = gu.text
                driver.find_element_by_xpath("//input[@type='image']").click()
                cityguparsing(cityname, guname)
            except:
                print(index)
    elif cityvalue == 27:
        for index in range(10,30):
            try:
                gu = driver.find_element_by_xpath("//option[@value='" + str(index*10) + "']")
                gu.click()
                guname = gu.text
                driver.find_element_by_xpath("//input[@type='image']").click()
                cityguparsing(cityname, guname)
            except:
                print(index)       
    elif cityvalue == 28:
        for index in range(10,27):
            try:
                gu = driver.find_element_by_xpath("//option[@value='" + str(index*10) + "']")
                gu.click()
                guname = gu.text
                driver.find_element_by_xpath("//input[@type='image']").click()
                cityguparsing(cityname, guname)
            except:
                print(index)       
    elif cityvalue == 29:
        for index in range(10,21):
            try:
                gu = driver.find_element_by_xpath("//option[@value='" + str(index*10) + "']")
                gu.click()
                guname = gu.text
                driver.find_element_by_xpath("//input[@type='image']").click()
                cityguparsing(cityname, guname)
            except:
                print(index) 
    elif cityvalue == 30:
        for index in range(10,24):
            try:
                gu = driver.find_element_by_xpath("//option[@value='" + str(index*10) + "']")
                gu.click()
                guname = gu.text
                driver.find_element_by_xpath("//input[@type='image']").click()
                cityguparsing(cityname, guname)
            except:
                print(index)     
    elif cityvalue == 31:
        for index in range(10,21):
            try:
                gu = driver.find_element_by_xpath("//option[@value='" + str(index*10) + "']")
                gu.click()
                guname = gu.text
                driver.find_element_by_xpath("//input[@type='image']").click()
                cityguparsing(cityname, guname)
            except:
                print(index)
    elif cityvalue == 36:
        for index in range(10,13):
            try:
                gu = driver.find_element_by_xpath("//option[@value='" + str(index*10) + "']")
                gu.click()
                guname = gu.text
                driver.find_element_by_xpath("//input[@type='image']").click()
                cityguparsing(cityname, guname)
            except:
                print(index)                   
    elif cityvalue == 41:
        for index in range(10,84):
            try:
                gu = driver.find_element_by_xpath("//option[@value='" + str(index*10) + "']")
                gu.click()
                guname = gu.text
                driver.find_element_by_xpath("//input[@type='image']").click()
                cityguparsing(cityname, guname)
            except:
                print(index)     
    elif cityvalue == 42:
        for index in range(10,24):
            try:
                gu = driver.find_element_by_xpath("//option[@value='" + str(index*10) + "']")
                gu.click()
                guname = gu.text
                driver.find_element_by_xpath("//input[@type='image']").click()
                cityguparsing(cityname, guname)
            except:
                print(index)   
        for index in range(72,84):
            try:
                gu = driver.find_element_by_xpath("//option[@value='" + str(index*10) + "']")
                gu.click()
                guname = gu.text
                driver.find_element_by_xpath("//input[@type='image']").click()
                cityguparsing(cityname, guname)
            except:
                print(index)     
    elif cityvalue == 43:
        for index in range(10,16):
            try:
                gu = driver.find_element_by_xpath("//option[@value='" + str(index*10) + "']")
                gu.click()
                guname = gu.text
                driver.find_element_by_xpath("//input[@type='image']").click()
                cityguparsing(cityname, guname)
            except:
                print(index)   
        for index in range(71,81):
            try:
                gu = driver.find_element_by_xpath("//option[@value='" + str(index*10) + "']")
                gu.click()
                guname = gu.text
                driver.find_element_by_xpath("//input[@type='image']").click()
                cityguparsing(cityname, guname)
            except:
                print(index)    
    elif cityvalue == 44:
        for index in range(12,28):
            try:
                gu = driver.find_element_by_xpath("//option[@value='" + str(index*10) + "']")
                gu.click()
                guname = gu.text
                driver.find_element_by_xpath("//input[@type='image']").click()
                cityguparsing(cityname, guname)
            except:
                print(index)   
        for index in range(71,84):
            try:
                gu = driver.find_element_by_xpath("//option[@value='" + str(index*10) + "']")
                gu.click()
                guname = gu.text
                driver.find_element_by_xpath("//input[@type='image']").click()
                cityguparsing(cityname, guname)
            except:
                print(index)     
    elif cityvalue == 45:
        for index in range(10,22):
            try:
                gu = driver.find_element_by_xpath("//option[@value='" + str(index*10) + "']")
                gu.click()
                guname = gu.text
                driver.find_element_by_xpath("//input[@type='image']").click()
                cityguparsing(cityname, guname)
            except:
                print(index)   
        for index in range(71,81):
            try:
                gu = driver.find_element_by_xpath("//option[@value='" + str(index*10) + "']")
                gu.click()
                guname = gu.text
                driver.find_element_by_xpath("//input[@type='image']").click()
                cityguparsing(cityname, guname)
            except:
                print(index) 
    elif cityvalue == 46:
        for index in range(10,24):
            try:
                gu = driver.find_element_by_xpath("//option[@value='" + str(index*10) + "']")
                gu.click()
                guname = gu.text
                driver.find_element_by_xpath("//input[@type='image']").click()
                cityguparsing(cityname, guname)
            except:
                print(index)   
        for index in range(71,92):
            try:
                gu = driver.find_element_by_xpath("//option[@value='" + str(index*10) + "']")
                gu.click()
                guname = gu.text
                driver.find_element_by_xpath("//input[@type='image']").click()
                cityguparsing(cityname, guname)
            except:
                print(index)    
    elif cityvalue == 47:
        for index in range(10,30):
            try:
                gu = driver.find_element_by_xpath("//option[@value='" + str(index*10) + "']")
                gu.click()
                guname = gu.text
                driver.find_element_by_xpath("//input[@type='image']").click()
                cityguparsing(cityname, guname)
            except:
                print(index)   
        for index in range(72,95):
            try:
                gu = driver.find_element_by_xpath("//option[@value='" + str(index*10) + "']")
                gu.click()
                guname = gu.text
                driver.find_element_by_xpath("//input[@type='image']").click()
                cityguparsing(cityname, guname)
            except:
                print(index)  
    elif cityvalue == 48:
        for index in range(11,34):
            try:
                gu = driver.find_element_by_xpath("//option[@value='" + str(index*10) + "']")
                gu.click()
                guname = gu.text
                driver.find_element_by_xpath("//input[@type='image']").click()
                cityguparsing(cityname, guname)
            except:
                print(index)   
        for index in range(72,90):
            try:
                gu = driver.find_element_by_xpath("//option[@value='" + str(index*10) + "']")
                gu.click()
                guname = gu.text
                driver.find_element_by_xpath("//input[@type='image']").click()
                cityguparsing(cityname, guname)
            except:
                print(index)     
    elif cityvalue == 50:
        for index in range(10,14):
            try:
                gu = driver.find_element_by_xpath("//option[@value='" + str(index*10) + "']")
                gu.click()
                guname = gu.text
                driver.find_element_by_xpath("//input[@type='image']").click()
                cityguparsing(cityname, guname)
            except:
                print(index)                                          
    #for index in range(11, 95):
        #try:
            #gu = driver.find_element_by_xpath("//option[@value='" + str(index*10) + "']")
            #gu.click()
            #guname = gu.text
            #driver.find_element_by_xpath("//input[@type='image']").click()
            #cityguparsing(cityname, guname)
        #except:
            #print(index)

#option value가 홀수 일 때      
def setHolGu(cityvalue):
    
    cityname = setCityName(cityvalue)
    
    tmp = []
    
    if cityvalue == 11:
        tmp = [215,305,545]
        for index in tmp:
            gu = driver.find_element_by_xpath("//option[@value='" + str(index) + "']")
            gu.click()
            guname = gu.text
            driver.find_element_by_xpath("//input[@type='image']").click()
            cityguparsing(cityname, guname)
    elif cityvalue == 26:
        tmp = [710]
        for index in tmp:
            gu = driver.find_element_by_xpath("//option[@value='" + str(index) + "']")
            gu.click()
            guname = gu.text
            driver.find_element_by_xpath("//input[@type='image']").click()
            cityguparsing(cityname, guname)
    elif cityvalue == 27:
        tmp = [710]
        for index in tmp:
            gu = driver.find_element_by_xpath("//option[@value='" + str(index) + "']")
            gu.click()
            guname = gu.text
            driver.find_element_by_xpath("//input[@type='image']").click()
            cityguparsing(cityname, guname)
    elif cityvalue == 28:
        tmp = [185,237,245,710,720]
        for index in tmp:
            gu = driver.find_element_by_xpath("//option[@value='" + str(index) + "']")
            gu.click()
            guname = gu.text
            driver.find_element_by_xpath("//input[@type='image']").click()
            cityguparsing(cityname, guname)
    elif cityvalue == 29:
        tmp = [155]
        for index in tmp:
            gu = driver.find_element_by_xpath("//option[@value='" + str(index) + "']")
            gu.click()
            guname = gu.text
            driver.find_element_by_xpath("//input[@type='image']").click()
            cityguparsing(cityname, guname)
    elif cityvalue == 31:
        tmp = [710]
        for index in tmp:
            gu = driver.find_element_by_xpath("//option[@value='" + str(index) + "']")
            gu.click()
            guname = gu.text
            driver.find_element_by_xpath("//input[@type='image']").click()
            cityguparsing(cityname, guname)        
    elif cityvalue == 41:
        tmp = [111,113,115,117,131,133,135,171,173,195,197,199,271,273,281,285,287,461,463,465]
        for index in tmp:
            gu = driver.find_element_by_xpath("//option[@value='" + str(index) + "']")
            gu.click()
            guname = gu.text
            driver.find_element_by_xpath("//input[@type='image']").click()
            cityguparsing(cityname, guname)
    elif cityvalue == 43:
        tmp = [111,112,113,114]
        for index in tmp:
            gu = driver.find_element_by_xpath("//option[@value='" + str(index) + "']")
            gu.click()
            guname = gu.text
            driver.find_element_by_xpath("//input[@type='image']").click()
            cityguparsing(cityname, guname)
    elif cityvalue == 44:
        tmp = [131,133,825]
        for index in tmp:
            gu = driver.find_element_by_xpath("//option[@value='" + str(index) + "']")
            gu.click()
            guname = gu.text
            driver.find_element_by_xpath("//input[@type='image']").click()
            cityguparsing(cityname, guname)
    elif cityvalue == 45:
        tmp = [111,113]
        for index in tmp:
            gu = driver.find_element_by_xpath("//option[@value='" + str(index) + "']")
            gu.click()
            guname = gu.text
            driver.find_element_by_xpath("//input[@type='image']").click()
            cityguparsing(cityname, guname)
    elif cityvalue == 47:
        tmp = [111,113]
        for index in tmp:
            gu = driver.find_element_by_xpath("//option[@value='" + str(index) + "']")
            gu.click()
            guname = gu.text
            driver.find_element_by_xpath("//input[@type='image']").click()
            cityguparsing(cityname, guname)
    elif cityvalue == 48:
        tmp = [121,123,125,127,129]
        for index in tmp:
            gu = driver.find_element_by_xpath("//option[@value='" + str(index) + "']")
            gu.click()
            guname = gu.text
            driver.find_element_by_xpath("//input[@type='image']").click()
            cityguparsing(cityname, guname)