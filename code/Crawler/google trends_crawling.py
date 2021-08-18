from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver_path = '../../resource/exe/chromedriver.exe'
driver = webdriver.Chrome(driver_path)
action = ActionChains(driver)


#######구글트렌드 페이지 오픈

#google trends india page
baseUrl = 'https://trends.google.com/trends/?geo=IN'
driver.get(baseUrl)
time.sleep(1)
#검색어 5개 입력 and ENTER
searchbox = driver.find_element_by_css_selector('#input-254')
keywords = "bmi,muscle,weight loss,gym,body mass"
searchbox.send_keys(keywords)
searchbox.send_keys(Keys.ENTER)
time.sleep(4)
#날짜 설정 팝업 띄우기
datesetting1 = driver.find_element_by_xpath('//*[@id="select_10"]').click()
time.sleep(1)
datesetting2 = driver.find_element_by_xpath('//*[@id="select_option_22"]').click()

#임시 테스트(나중에 지우기!!)

#원하는 날짜 입력하기


# csv download
download_btn = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/md-content/div/div/div[1]/trends-widget/ng-include/widget/div/div/div/widget-actions/div/button[1]')
download_btn.click()

