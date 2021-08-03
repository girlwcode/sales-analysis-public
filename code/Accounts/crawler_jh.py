import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver_path = '../chromedriver.exe'
url = 'https://www.google.co.kr/maps/search/hospital+in+mumbai+/@19.0513695,72.8289603,12z/data=!3m1!4b1?hl=ko'

browser = webdriver.Chrome(executable_path=driver_path) #Chrome driver
browser.get(url)

# get page html전체 따옴
page = browser.page_source
# browser.quit() # 코드
soup = BeautifulSoup(page, "html.parser") #html파싱하겠다~
# print(soup) #코드

def searchPlace():
    place = driver_path.find_element_by_classname("tactile-searchbox-input")
    place.send_keys("hospital in mumbai")
    submit = driver_path.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
    submit.click()
    time.sleep(2)

searchPlace()

SCROLL_PAUSE_SEC = 2

# 스크롤 높이 가져옴
last_height = driver_path.execute_script("return document.body.scrollHeight")

while True:
    # 끝까지 스크롤 다운
    driver_path.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 2초 대기
    time.sleep(SCROLL_PAUSE_SEC)

    # 스크롤 다운 후 스크롤 높이 다시 가져옴
    new_height = driver_path.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

def scrapperPlace():

    select_hospt = driver_path.find_elements_by_css_selector("a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd")
    for each_hosp in select_hospt:
        each_hosp.click()
        time.sleep(2)  #병원 리스트 중 한개 클릭

        select_name = driver_path.find_element_by_css_selector("x3AX1-LfntMc-header-title-title gm2-headline-5")
        select_name.click()
        time.sleep(2)  #개별 병원 클릭 후 상호명 가져옴

        select_adds = driver_path.find_element_by_css_selector("QSFF4-text gm2-body-2")
        select_adds.click()
        time.sleep(2)  # 개별 병원의 주소 가져옴

