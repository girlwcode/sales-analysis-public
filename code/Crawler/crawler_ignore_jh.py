import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import pyautogui
import time

driver_path = '../../resource/exe/chromedriver.exe'
url = 'https://www.google.co.kr/maps/@19.0753242,72.7389776,11z?hl=ko'

search_name = "hospital in mumbai"
browser = webdriver.Chrome(executable_path = driver_path) #Chrome driver
browser.get(url)

page = browser.page_source
soup = BeautifulSoup(page, "html.parser")   #html파싱하겠다~
data1 = []
data2 = []

def searchPlace():
    searchBox = browser.find_element_by_id("searchboxinput")
    searchBox.send_keys(search_name)
    submit = browser.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
    submit.click()
    time.sleep(2)

    pyautogui.moveTo(178, 429)  #마우스 좌표 이동




    # while True:
    #     SCROLL_PAUSE_SEC = 1
    #     # 끝까지 스크롤 다운
    #     browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #
    #     # 1초 대기
    #     time.sleep(SCROLL_PAUSE_SEC)
    #
    #     # 스크롤 다운 후 스크롤 높이 다시 가져옴
    #     new_height = browser.execute_script("return document.body.scrollHeight")
    #     last_height = new_height
    #     if new_height == last_height:
    #         break


searchPlace()

itemlist = browser.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[4]/div[1]')

for _ in range(4):  # 스크롤 끝까지 다운
    browser.execute_script('argument[0].scrollBy(0,1000)', itemlist)
    time.sleep(1)

for i in range(22):
    try:
        html = browser.page_source
        soup = BeautifulSoup(html, "html.parser")
        tmp = soup.select('.a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd')  # 한 페이지에 병원 정보 20개 있으니까 20개 찾아짐
        data1.extend(tmp)  # data라는 리스트에 추가
    except:
        break
# print(data1)

dataList = []
for tmp in data1:   # data1에서 하나씩 뽑아온 다음에
    data_dict = {'name' : tmp['aria-label'], 'link': tmp['href']}  # 병원이름과 병원링크를 딕셔너리로 저장한 뒤
    dataList.append(data_dict)   # 리스트에 추가.
print(dataList)
# data_df = pd.DataFrame(data1)
# data_df.head(10)
# dataList.to_csv('./hospital list.csv')

##병원 하나하나 주소 가져오기


