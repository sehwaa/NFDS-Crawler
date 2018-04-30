#coding: utf-8

#월 별 날짜 계산
def lastday(year, month):
    
    #1~12까지 마지막 날 초기화
    day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    #2월이면 윤년계산
    if month == 2 :
        if year % 4 == 0 :
            day[1] = 29
        else :
            day[1] = 28
    
    #1~12월까지
    if month < 10 :
        startdate = str(year) + "-0" + str(month) + "-01"
        enddate = str(year) + "-0" + str(month) + "-" + str(day[month - 1])
    else :
        startdate = str(year) + "-" + str(month) + "-01"
        enddate = str(year) + "-" + str(month) + "-" + str(day[month - 1]) 
            
    date = [startdate, enddate]
    return date

    
    