import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import time
#구글 드라이버를 실행시키기위한 준비
driver_path = '../../resource/exe/chromedriver.exe'
url = 'https://www.google.co.kr/maps/@19.0753242,72.7389776,11z?hl=ko'
browser = webdriver.Chrome(executable_path = driver_path) #Chrome driver
dataList=[]
csv={'Category':[]}
#search_name으로 검색 수행
def searchPlace(search_name):
        searchBox = browser.find_element_by_id("searchboxinput")
        searchBox.send_keys(search_name)
        submit = browser.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
        submit.click()
        time.sleep(2)
#dataList는 봇솔 등의 크롤러를 통해 얻은 사업장이름들이 담긴 리스트
def scrapperPlace(dataList):
    try:
        for data in dataList:
            #해당 키워드를 검색
            searchPlace(data)
        #카테고리 긁어오기
            classes=browser.find_elements_by_class_name('widget-pane-link')
            for target in classes:
                if 'hospital' in target.text or 'Hospital' in target.text:
                    csv['Category'].append(target.text)
                    print(target.text)
                    break

            #카테고리의 고유 jsaction은 pane.rating.category
            browser.back()
            browser.implicitly_wait(time_to_wait=5)
    #만약에 이름으로 검색을 수행했을 때 해당 사업장 세부사항 페이지로 바로 가는게 아니라 유사 사업장 리스트를 띄울경우 그냥 맨첫번쨰 카드로 들어감
    except:
            details=browser.find_elements_by_class_name('a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd')
            detail_button=details[3]
            detail_button.click()# j번쨰 뷰로 들어감.
            scrapperPlace()