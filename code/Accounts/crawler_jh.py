import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver_path = '../../resource/exe/chromedriver.exe'
url = 'https://www.google.co.kr/maps/@19.0753242,72.7389776,11z?hl=ko'

search_name = "hospital in mumbai"
browser = webdriver.Chrome(executable_path=driver_path) #Chrome driver
browser.get(url)

# get page html 전체 따옴
page = browser.page_source
# browser.quit() # 코드
soup = BeautifulSoup(page, "html.parser")   #html파싱하겠다~
# print(soup) #코드


def searchPlace():
    searchBox = browser.find_element_by_id("searchboxinput")
    searchBox.send_keys(search_name)
    submit = browser.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button").click()
    time.sleep(2)

searchPlace()


def scrapperPlace():
    search_output = {'Title':[],'   Address':[  ]}
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")  #스크롤 다운
    select_hospt = browser.find_elements_by_css_selector("a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd")

    for each_hosp in select_hospt:
        each_hosp.click()
        time.sleep(5)  #병원 리스트 중 한개 클릭

        select_name = browser.find_element_by_css_selector("x3AX1-LfntMc-header-title-title gm2-headline-5")
        search_output.Title.append(select_name)
        select_name.click()
        time.sleep(5)  #개별 병원 클릭 후 상호명 가져옴

        select_adds = browser.find_element_by_css_selector("QSFF4-text gm2-body-2")
        search_output.Address.append(select_name)
        select_adds.click()
        time.sleep(5)  # 개별 병원의 주소 가져옴

    return search_output
scrapperPlace()

output = scrapperPlace()
scrapper = pd.DataFrame(output)
search_name = search_name.replace(" ","_")
scrapper.to_csv(search_name+".csv", index=False)


