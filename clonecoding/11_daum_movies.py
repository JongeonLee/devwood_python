import requests
from bs4 import BeautifulSoup

for year in range(2016,2021):
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    images = soup.find_all('img',attrs = {'class':'thumb_img'})

    for idx, img in enumerate(images): #enumerae: index와 enumearte 속의 내용을 튜플 형태로 반환함 ex) (0, img1), (1,img2), ...
        img_url = img['src']
        if img_url.startswith('//'): #//로 시작할 겨우 https:를 붙여주는 역할
            img_url = 'https:' + img_url
        
        #print(img_url)
        img_res = requests.get(img_url)
        img_res.raise_for_status()

        with open('movie_{}_{}.jpg'.format(year, idx+1),'wb') as f:
            f.write(img_res.content)
        if idx >= 4:
            break