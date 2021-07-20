import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/list?titleId=675554'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
cartoons = soup.find_all('td', attrs= {'class':'title'})

        #만화 제목 + 링크 구하기

# title = cartoons[0].a.get_text()
# link = cartoons[0].a['href'] # 태그 안의 내용을 가져오려면 대괄호를 사용하면 됨

# print(title)
# print("https://comic.naver.com"+ link)
for c in cartoons:
    title = c.a.get_text()
    link = "https://comic.naver.com" + c.a['href']
    print(title)
    print(link)

        #평점 구하기 + 평균 평점 구하기
totar_rate = 0
ratings = soup.find_all('div', attrs={'class': 'rating_type'})
for rate in ratings:
    star = rate.find('strong').get_text()
    #다른 방법: star = rate.strong.get_text()
    print(star)
    totar_rate += float(star)
print('평균 평점:',totar_rate/len(ratings))
