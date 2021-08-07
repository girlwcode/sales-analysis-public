from selenium import webdriver
from selenium.webdriver import ActionChains
import pandas as pd
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
    # 주소있는 layout까지 scrap
    end = browser.find_element_by_class_name('aopO7e-divider')
    scroll = ActionChains(browser).move_to_element(end)
    scroll.perform()
    # Company_Name
    name = browser.find_element_by_class_name('x3AX1-LfntMc-header-title-title.gm2-headline-5')
    search_result["Company_Name"].append(name.text)
    # Category
    categories = browser.find_elements_by_class_name('h0ySl-wcwwM-E70qVe')
    search_result["Category"].append(categories[1].text)
    # Address
    elements = browser.find_elements_by_class_name('rogA2c')
    for element in elements:
        if 'covid' in element.text.lower():
            continue
        else:
            search_result["Address"].append(element.text)
            break



# Main
search_result = {'Company_Name': [], 'Category': [], 'Address': [], 'Url': []}

googleMap_url = 'https://www.google.co.kr/maps/@37.053745,125.6553969,5z?hl=en'
driverPath = '../../resource/exe/chromedriver.exe'

browser = webdriver.Chrome(executable_path=driverPath)
browser.get(googleMap_url)
time.sleep(3)
# 검색어
search_keyword = 'hospital in Goa, India'
searching(search_keyword)

while True:
    scrolling()
    time.sleep(2)
    search_list = browser.find_elements_by_class_name('a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd')

    browser_company = webdriver.Chrome(executable_path=driverPath)
    # 검색페이지 1개당 검색결과 20개
    for i, company_url in enumerate(search_list):
        # Company_url 열기
        browser_company.get(company_url.get_attribute('href'))
        time.sleep(3)
        # 스크롤
        scrolling_company()
        # 데이터 가져오기
        crawling(browser_company)
        search_result['Url'].append(company_url.get_attribute('href'))
    print(len(search_list))
    browser_company.close()

    # 다음페이지있으면 넘어가기
    try:
        browser.find_element_by_xpath('//*[@id="ppdPk-Ej1Yeb-LgbsSe-tJiF1e"]/img').click()
    except:
        browser.close()
        print("Crawling END")
        break

# Data phrasing
result = pd.DataFrame(search_result)
save_dir = '../../resource/CrawlingData/'+search_keyword+'.csv'
result.to_csv(save_dir, index=False)