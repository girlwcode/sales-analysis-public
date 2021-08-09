from selenium import webdriver
from selenium.webdriver import ActionChains
import pandas as pd
import numpy as np
import time


# 검색창 입력 & 검색버튼 클릭
def searching(search_keyword):
    browser.find_element_by_id("searchboxinput").send_keys(search_keyword)
    browser.find_element_by_class_name('searchbox-searchbutton').click()
    time.sleep(3)


# 검색결과 스크롤
def scrolling():
    itemlist = browser.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[4]/div[1]')
    for _ in range(5):
        browser.execute_script('arguments[0].scrollBy(0, 1000)', itemlist)
        time.sleep(1)


# 데이터 가져오기
def crawling(browser):
    # 스크롤 한번 움직임
    start = browser.find_element_by_class_name('x3AX1-LfntMc-header-title-title.gm2-headline-5')
    scroll = ActionChains(browser).move_to_element(start)
    scroll.perform()
    time.sleep(1)
    # Company_Name
    name = browser.find_element_by_class_name('x3AX1-LfntMc-header-title-title.gm2-headline-5')
    data_dict['Company_Name'] = name.text
    # Category
    categories = browser.find_elements_by_class_name('h0ySl-wcwwM-E70qVe')
    try:
        data_dict['Category'] = categories[1].text
    except:
        data_dict['Category'] = np.nan
    # Address
    elements = browser.find_elements_by_class_name('rogA2c')
    for element in elements:
        if 'covid' in element.text.lower():
            continue
        else:
            data_dict['Address'] = element.text
            break


# Main
search_result = pd.DataFrame(columns=['Company_Name', 'Category', 'Address', 'Url'])

googleMap_url = 'https://www.google.co.kr/maps/@37.053745,125.6553969,5z?hl=en'
driverPath = '../../resource/exe/chromedriver.exe'

browser = webdriver.Chrome(executable_path=driverPath)
browser.get(googleMap_url)
time.sleep(3)
# 검색어
search_keyword = 'hospital in Jammu and Kashmir, India'
searching(search_keyword)

while True:
    time.sleep(3)
    scrolling()
    time.sleep(2)
    search_list = browser.find_elements_by_class_name('a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd')
    browser_company = webdriver.Chrome(executable_path=driverPath)
    # 검색페이지 1개당 검색결과 20개
    for i, company_url in enumerate(search_list):
        data_dict = dict.fromkeys(['Company_Name', 'Category', 'Address', 'Url'])
        # Company_url 열기
        browser_company.get(company_url.get_attribute('href'))
        time.sleep(5)
        # 데이터 가져오기
        crawling(browser_company)
        data_dict['Url'] = company_url.get_attribute('href')
        # 데이터프레임에 row 추가
        search_result = search_result.append(data_dict, ignore_index=True)
        print(data_dict)

    print(len(search_list))     # list 하나 완료
    browser_company.close()

    # 다음페이지있으면 넘어가기
    try:
        browser.find_element_by_xpath('//*[@id="ppdPk-Ej1Yeb-LgbsSe-tJiF1e"]/img').click()
    except:
        browser.close()
        print("Crawling END")
        break

# Data phrasing
save_dir = '../../resource/CrawlingData/' + search_keyword + '.csv'
search_result.to_csv(save_dir, index=False)
