import requests
from bs4 import BeautifulSoup
from selenium import webdriver
# 동적 페이지(ex. 스크롤을 내림에 따라 컨텐츠가 계속 늘어남)

browser = webdriver.Chrome('C:\devwood\devwood_python\chromedriver.exe')
browser.maximize_window()

# 페이지 이동
url = 'https://play.google.com/store/movies/top'
browser.get(url)

#스크롤 내리기
browser.execute_script('window.scrollTo(0,1080)') #1080: 윈도우 pc의 해상도 정도 (1920 * 1080-높이)

#화면 가장 아래로 스크롤 내리기
#browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

import time
interval = 2 # 2초에 한 번씩 스크롤을 내림

#현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script('return document.body.scrollHeight')

#반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    
    #페이지 로딩 대기
    time.sleep(interval)

    #현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script('return document.body.scrollHeight')

    if curr_height == prev_height: # 더 이상 내릴 수 없다는 의미
        break

    prev_height = curr_height


soup = BeautifulSoup(browser.page_source, 'lxml')
movies = soup.find_all('div', attrs ={'class':'Vpfmgd'})
# class를 리스트로 감쌀 시 or 개념으로 사용됨(클래스 이름이 A이거나 B 인것 모두 가져옴)

for movie in movies:
    title = movie.find('div', attrs={'class':'WsMG1c nnK0zc'}).get_text()
    
    #할인 전 가격
    original_price = movie.find('span', attrs={'class':'SUZt4c djCuy'})

    if original_price:
        original_price = original_price.get_text()
    else:
        continue
    
    #할인 된 가격
    price = movie.find('span', attrs={'class':"VfPpfd ZdBevf i5DZme"}).get_text()

    #할인 영화 링크
    link =  movie.find('a', attrs={'class':"JC71ub"})['href']

    print(f'제목: {title}')
    print(f'할인 전 금액: {original_price}')
    print(f'할인 후 금액: {price}')
    print('링크: https://play.google.com' + str(link))
    print('-'* 118)

browser.quit()
