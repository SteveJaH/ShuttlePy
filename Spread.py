import time
import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException

now = datetime.datetime.now()
dateformat = str(now.year) + str(now.month).zfill(2) +  str(now.day+2).zfill(2)

f = open("Reserv.txt", 'r')
lines = f.readlines()
user_id = lines[3].rstrip("\n")
password = lines[5].rstrip("\n")
numbers = int(lines[38])
reslist = lines[45: 45+numbers]
for i in range(0, numbers):
    reslist[i] = reslist[i].split()
f.close()

print(dateformat)
wday = 0
IS = 0
Busnumber = 0

week = {0 : 'Mon', 1 : 'Tue', 2 : 'Wed', 3 : 'Thu', 4 : 'Fri', 5 : 'Sat', 6 : 'Sun'}


def login(driver, Id, Password):
    driver.get ("https://ysweb.yonsei.ac.kr/ysbus.jsp")
    driver.find_element_by_id("id").send_keys(id)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_class_name("submit").click()

def CondCheck(driver):
    driver.get("https://ysweb.yonsei.ac.kr/busTest/index2.jsp")
    count = 0

    #요일 선택
    date = Select(driver.find_element_by_css_selector('#selectedDate')).options
    datelist = []

    while (dateformat not in datelist)  and (count <= 20):
        date = Select(driver.find_element_by_css_selector('#selectedDate'))
        datelist = date.options
        print(datetime.datetime.now(), datelist, dateformat)
        time.sleep(0.2)
        driver.refresh()
        count = count + 1

    date = Select(driver.find_element_by_css_selector('#selectedDate'))
    datelist = date.options

    if(dateformat in datelist):
        #3번째 날 선택
        print("1111111111")
        date.select_by_value(dateformat)
        return 1
    else:
        print("Error : No date equal!\n")
        return 0

def reservation(driver, IS, Busnumber):

    driver.get("https://ysweb.yonsei.ac.kr/busTest/index2.jsp")

    #신촌 송도 송도 신촌
    if(IS==0): #신촌 송도
        IS = driver.find_element_by_css_selector('#pageid > div > ul.tab_info.ty2 > li:nth-child(1) > a').click()
    else: #(IS==1) #송도 신촌
        IS = driver.find_element_by_css_selector('#pageid > div > ul.tab_info.ty2 > li:nth-child(2) > a').click()

    date = Select(driver.find_element_by_css_selector('#selectedDate'))
    date.select_by_value(dateformat)

    #첫번째 tr:nth-child(*) 가 시간에 해당하는
    #변수 #pageid > div > div.table_box.tab_cont > table > tbody > tr:nth-child(8) > td:nth-child(5) > select
    select = Select(driver.find_element_by_css_selector('#pageid > div > div.table_box.tab_cont > table > tbody > tr:nth-child('+ str(Busnumber) + ') > td:nth-child(5) > select'))
    #"강의" 선택
    select.select_by_value('1')
    remain = driver.find_element_by_xpath('//*[@id="pageid"]/div/div[2]/table/tbody/tr[6]')
    print(remain)


    #신청 버튼; 마찬가지로 첫번째 tr:nth-child(*) 가 변수
    # #pageid > div > div.table_box.tab_cont > table > tbody > tr:nth-child(8) > td:nth-child(6) > span
    enter = driver.find_element_by_css_selector('#pageid > div > div.table_box.tab_cont > table > tbody > tr:nth-child(' + str(Busnumber) + ') > td:nth-child(6)').click()
    try:
        Alert(driver).accept()
    except NoAlertPresentException as e:
        print("FULL")

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver1 = webdriver.Chrome('chromedriver.exe', options=options)
login(driver1, user_id, password)

#if(CondCheck(driver1)==1):
for i in range(0, numbers):
    wday = reslist[i][0]
    IS = int(reslist[i][1])
    Busnumber = reslist[i][2]
    tw = datetime.datetime.now()+datetime.timedelta(days=2)
    if(tw.weekday()==int(wday)):
        reservation(driver1, IS, Busnumber)

driver1.get("https://ysweb.yonsei.ac.kr/busTest/reserveinfo2.jsp")


#pageid > div > div.table_box.tab_cont > table > tbody > tr:nth-child(2) > td:nth-child(6) > a
#//*[@id="pageid"]/div/div[2]/table/tbody/tr[2]/td[6]/a
#pageid > div > div.table_box.tab_cont > table > tbody > tr:nth-child(3) > td:nth-child(6) > span
#//*[@id="pageid"]/div/div[2]/table/tbody/tr[3]/td[6]/span


# IS, Busnumber
# 5 토요일 1 8 , 0 17
# 0 월요일 1 7 , 0 18
    
