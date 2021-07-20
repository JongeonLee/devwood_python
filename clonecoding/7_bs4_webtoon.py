import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

#네이버 웹툰 전체 제목 가져오기
cartoons = soup.find_all('a', attrs ={'class': 'title'}) #class 속성이 title인 모든 'a' element 반환 
# 그냥 find -> 조건을 만족하는 첫 번째 element
# find_all -> 조건을 만족하는 모든 element
for c in cartoons:
    print(c.get_text())