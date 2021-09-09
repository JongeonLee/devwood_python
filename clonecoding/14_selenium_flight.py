from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome('C:\devwood\devwood_python\chromedriver.exe')
browser.maximize_window() #창 크기 최대화

url = 'https://flight.naver.com/flights/'
browser.get(url)

browser.find_element_by_link_text('가는날 선택').click() #link_text -> 태그 내의 text를 이용해 찾음

#이번 달 27일, 28일 선택
browser.find_elements_by_link_text('27')[0].click() #index가 0 -> 이번 달
browser.find_elements_by_link_text('28')[1].click() #index가 1 -> 다음 달

#제주도 선택
browser.find_element_by_xpath('//*[@id="recommendationList"]/ul/li[1]/div/span').click()

#항공권 검색 클릭
browser.find_element_by_link_text('항공권 검색').click()
try:
    elem = WebDriverWait(browser,20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')))
    #WebDriverWait를 통해 브라우저를 최대 20초 동안 기다림, 그러나 10초 안에 XPATH에 해당하는 element가 나오면 바로 실행
    print(elem.text)
finally:
    browser.quit()

#첫 번쨰 결과 출력
# elem = browser.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')
# print(elem.text)