import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

#가져온 html 문서를 lxml모듈을 통해서 BeautifulSoup 객체로 만든 것 -> 모든 정보를 담고 있음

# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # 처음 발견되는 a element를 출력
# print(soup.a.attrs) # a element의 속성 정보를 출력
# print(soup.a['href']) # a element의 href 속성 '값' 정보를 출력

print(soup.find("a", attrs={'class': 'Nbtn_upload'}))  
# soup 객체 내의 a 태그 중 속성값(클래스)가 'Nbtn_upload'인 것을 반환함

# print(soup.find("li", attrs={'class': 'rank01'})): 너무 복잡 -> a 태그 내용만 있으면 됨
rank1 = soup.find("li", attrs={'class': 'rank01'}) 
rank1_a = soup.find("a", text="여신강림-166화") # rank1 안의 a 태그 내용 찾는 방법

print(rank1.a.get_text())

# 형제 태그들 사이에서 다음 형제의 내용을 가져올 수 있음
# print(rank1.next_sibling) # 형제들 사이에 다른게 끼어 있을 경우(개행 정보), 제대로 이루어지지 않을 수 있음
rank2 = rank1.next_sibling.next_sibling
print(rank2.a.get_text()) # 그럴 때에는 한 번 더 하면 됨
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text())

# 이전으로 돌아갈 수도 있음
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())

# 개행정보 무시하고 다음 형제 정보를 찾는 방법
rank2 = rank1.find_next_sibling("li")
print(rank2.a.get_text())

#형제들 정보를 한꺼번에 가져오는 방법
print(rank1.find_next_siblings('li'))