#coding: utf-8

from lastday import lastday
from date import setDate
from city import setCity
from gu import setGu, setHolGu
from parsing import dateparsing
    
if __name__ == "__main__" :
    
    #시 option value 리스트
    city_option_value = [11, 26, 27, 28, 29, 30, 31, 36, 41, 42, 43, 44, 45, 46, 47, 48, 50]
    
    #날짜 설정
    for year in range(2015, 2018):
        if year == 2017 :
            for month in range(1,7):
                startdate = lastday(year, month)[0]
                enddate = lastday(year, month)[1]
                setDate(startdate, enddate)
                #시, 동 설정
                for index in city_option_value:
                    dateparsing(startdate,enddate)
                    setCity(index)
                    setGu(index)
                    setHolGu(index)
        else :
            for month in range(1,9):
                startdate = lastday(year, month)[0]
                enddate = lastday(year, month)[1]
                setDate(startdate, enddate)
                for index in city_option_value:
                    dateparsing(startdate,enddate)
                    setCity(index)
                    setGu(index)
                    setHolGu(index)
            for month in range(9,13):
                startdate = lastday(year, month)[0]
                enddate = lastday(year, month)[1]
                setDate(startdate, enddate)
                for index in city_option_value:
                    dateparsing(startdate,enddate)
                    setCity(index)
                    setGu(index)
                    setHolGu(index)
                        
    