from selenium import webdriver
import time

# 크롬창(웹드라이버) 열기
driver = webdriver.Chrome("./chromedriver")

#키워드 입력
keyword='hospital'
state='in mumbai'

# 구글 지도 접속하기
driver.get("https://www.google.com/maps/")

#검색창에 키워드를 침
searchbox = driver.find_element_by_css_selector("input#searchboxinput")
searchbox.send_keys(keyword+state)

# 검색버튼 누르기
searchbutton = driver.find_element_by_css_selector("button#searchbox-searchbutton")
searchbutton.click()

for i in range(10000):
    # 시간 지연
    time.sleep(3)

    # 컨테이너(사업장명) 데이터 수집 // div.section-result-content
    stores = driver.find_elements_by_css_selector("div.section-result-content")
    
    for s in stores:
        # 사업장 이름 데이터 수집 // h3.section-result-title
        title = s.find_element_by_css_selector("h3.section-result-title").text

        # 카테고리 수집 // span.cards-rating-score
        # 카테고리가 없는 경우 에러 발산
        #   ​
        # 가게 주소 데이터 수집 // span.section-result-location
        addr = s.find_element_by_css_selector("span.section-result-location").text

        print(title, "/", '           ', "/", addr)
    #​
    # 다음페이지 버튼 클릭 하기
    # 다음페이지가 없는 경우(데이터 수집 완료) 에러 처리
    try:
        nextpage = driver.find_element_by_css_selector("button#n7lv7yjyC35__section-pagination-button-next")
        nextpage.click()
    except:
        print("데이터 수집 완료.")
        break