from selenium import webdriver
import time
#웹드라이버 연결
driver = webdriver.Chrome("../../resource/exe/chromedriver.exe")
#키워드 입력
keyword='hospital'
state='Goa'
#그 전에 구글 로그인 필요.로그인 시 해당 계정의 선호 언어를 영어로 바꿔야 함.

#해당 url로 이동
driver.get("https://www.google.com/maps/")
#키워드를 검색창에 씀
searchbox = driver.find_element_by_css_selector("input#searchboxinput")
searchbox.send_keys(keyword+' in '+state)
# 검색버튼 누르기
searchbutton = driver.find_element_by_css_selector("button#searchbox-searchbutton")
searchbutton.click()

#2:26에 try 박아봄
companies=[]
company={'Company_name1':'','company_name2':'Category','Address':''}
for i in range(100000):
    #창이 뜰 시간동안 대기
    driver.implicitly_wait(time_to_wait=2)
    #페이지 스크롤을 끝까지 내리고 대기
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    driver.implicitly_wait(time_to_wait=3)

        #검색한 결과를 하나씩 클릭해서 데이터 긁어옴
        
        #요소의 xpath
# //*[@id="pane"]/div/div[1]/div/div/div[4]/div[1]/div[3]/div/a
# //*[@id="pane"]/div/div[1]/div/div/div[4]/div[1]/div[5]/div/a
# //*[@id="pane"]/div/div[1]/div/div/div[4]/div[1]/div[41]/div/a
#다음페이지
#//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/h1/span[1]
    for j in range(3,42,2):
        #사업장 클릭
        #//*[@id="pane"]/div/div[1]/div/div/div[4]/div[1]/div[3]/div/a

        detail_button=driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[4]/div[1]/div['+str(j)+']/div/a')
        detail_button.click()
        driver.implicitly_wait(time_to_wait=1)
        #사업장명(거의 영어)
        company_name=driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/h1/span[1]')
        companies.append(company_name.text)

        print(companies)
        #사업장명2(사업장명이 인도어일 때 대체용.아니면 노답)
        company_name2=driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/h2/span')
        companies.append(company_name2.text)
        #카테고리
        category=driver.find_element_by_xpath('//*[contains(@jsaction,"pane.rating.category")]')
        companies.append(category.text)
        
        #주소
        #<div jstcache="1109" class="QSFF4-text gm2-body-2" jsan="7.QSFF4-text,7.gm2-body-2">Mapusa Jamatkhana Road, Peddem, Mapusa, Goa 403507, India</div>
        address=driver.find_element_by_xpath()
        companies.append(address.text)


        #페이지 돌아가기
        print(companies)
        page_back=driver.find_element_by_xpath('//*[@id="omnibox-singlebox"]/div[1]/div[4]/div/div[1]/div/div/button/span')
        page_back.click()
    try:
        #다음페이지로 넘어감
        nextbutton = driver.find_element_by_xpath('//*[@id="ppdPk-Ej1Yeb-LgbsSe-tJiF1e"]/img')
        nextbutton.click()
    except:
        print("loop ended")
        break