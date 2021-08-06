from selenium import webdriver
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
    for _ in range(4):
        browser.execute_script('arguments[0].scrollBy(0, 1000)', itemlist)
        time.sleep(2)
    time.sleep(3)


# 데이터 가져오기
def crawling(browser):
    # Company_Name
    name = browser.find_element_by_class_name('x3AX1-LfntMc-header-title-title.gm2-headline-5')
    # print(name.text)
    search_result["Company_Name"].append(name.text)
    # Category
    category = browser.find_elements_by_class_name('gm2-body-2')
    search_result["Category"].append(category[1].text)
    # print(category[1].text)
    # Address
    elements = browser.find_elements_by_class_name('AeaXub')
    if "covid" in elements[0].text.lower():
        if "covid" in elements[1].text.lower():
            # print(elements[2].text)
            search_result["Address"].append(elements[2].text)
        else:
            # print(elements[1].text)
            search_result["Address"].append(elements[1].text)
    else:
        # print(elements[0].text)
        search_result["Address"].append(elements[0].text)



# main
search_result = {'Company_Name': [], 'Category': [], 'Address': []}

googleMap_url = 'https://www.google.co.kr/maps/@37.053745,125.6553969,5z?hl=en'
driverPath = '../../resource/exe/chromedriver.exe'

browser = webdriver.Chrome(executable_path=driverPath)
browser.get(googleMap_url)
time.sleep(3)

search_keyword = 'hospital in Goa, India'
searching(search_keyword)

while True:
    scrolling()
    search_list = browser.find_elements_by_class_name('a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd')

    browser_company = webdriver.Chrome(executable_path=driverPath)
    # 검색페이지 1개 당 검색결과 20개
    for i, company_url in enumerate(search_list):
        # print(i, company_url.get_attribute('href'))
        browser_company.get(company_url.get_attribute('href'))
        time.sleep(2)
        crawling(browser_company)
    browser_company.close()
    # 다음페이지있으면 넘어가기
    try:
        browser.find_element_by_xpath('//*[@id="ppdPk-Ej1Yeb-LgbsSe-tJiF1e"]/img').click()
    except:
        browser.close()
        print("END")
        break

result = pd.DataFrame(search_result)
save_dir = '../../resource/CrawlingData/'+search_keyword+'.csv'
result.to_csv(save_dir, index=False)