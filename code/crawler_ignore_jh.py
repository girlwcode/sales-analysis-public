import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver_path = '../resource/exe/chromedriver.exe'
url = 'https://www.google.co.kr/maps/@19.0753242,72.7389776,11z?hl=ko'

search_name = "hospital in mumbai"
browser = webdriver.Chrome(executable_path=driver_path) #Chrome driver
browser.get(url)

page = browser.page_source
soup = BeautifulSoup(page, "html.parser")   #html파싱하겠다~

def searchPlace():
    searchBox = browser.find_element_by_id("searchboxinput")
    searchBox.send_keys(search_name)
    submitClick = browser.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button").click()
    time.sleep(2)

searchPlace()

def scrapperPlace():
    search_output = {'Title':[],'   Address':[  ]}
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")  #스크롤 끝까지 다운

    select_hospt = browser.find_elements_by_css_selector("a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd")


