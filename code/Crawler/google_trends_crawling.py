from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time


def input_date(year, month): # 윤년xxxxx, month는 1월부터
    start_date = str(year)+'.'+str(month)+'.01'
    end_date = str(year)+'.'+str(month)+'.'
    if month < 10:
        if month%2 == 1:    # 홀수달 31일(9월30일)
            if month == 9:
                end_date += '30'
            else:
                end_date += '31'
        else:   # 짝수달 30일(2월28일,8월31일)
            if month == 2:
                end_date += '28'
            elif month == 8:
                end_date += '30'
            else:
                end_date += '31'
    else:
        if month%2 == 0:    # 짝수달 31일
            end_date += '31'
        else:   # 홀수달 30일
            end_date += '30'

    return start_date, end_date



# Main

driver_path = '../../resource/exe/chromedriver.exe'
driver = webdriver.Chrome(driver_path)
# action = ActionChains(driver)

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

for month in range(1,13):
    year = 2017
    start_date, end_date = input_date(year, month)
    #날짜 설정 팝업 띄우기
    datesetting1 = driver.find_element_by_xpath('//*[@id="select_10"]').click()
    time.sleep(1)
    datesetting2 = driver.find_element_by_xpath('//*[@id="select_option_22"]').click()
    time.sleep(1)
    #원하는 날짜 입력하기
    date_container = driver.find_elements_by_class_name('md-datepicker-input-container')
    start = date_container[0].find_element_by_class_name('md-datepicker-input')
    start.clear()
    start.click()
    time.sleep(1)
    start.send_keys(start_date)
    end = date_container[1].find_element_by_class_name('md-datepicker-input')
    end.clear()
    end.click()
    time.sleep(1)
    end.send_keys(end_date)
    # 확인
    time.sleep(2)
    buttons = driver.find_elements_by_class_name('custom-date-picker-dialog-button.md-button.md-ink-ripple')
    ok_button = buttons[1]
    ok_button.click()
    time.sleep(3)
    #csv download
    download_btn = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/md-content/div/div/div[1]/trends-widget/ng-include/widget/div/div/div/widget-actions/div/button[1]')
    download_btn.click()

