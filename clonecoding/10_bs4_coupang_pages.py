import requests
import re
from bs4 import BeautifulSoup
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
for i in range(1,6): 
    url = 'https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0\
    &page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor='.format(i)
    print('현재 페이지:',i)
    res = requests.get(url,headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    items = soup.find_all('li', attrs={'class':re.compile('^search-product')}) 
    for item in items:
        ad_badge = item.find('span',attrs={'class':'ad-badge-text'})
        if ad_badge:
            continue

        name = item.find('div',attrs={'class':'name'}).get_text() # 제품명
        if 'Apple' in name:
            continue
        
        price = item.find('strong',attrs={'class':'price-value'}) # 가격
        if price:
            price = item.find('strong',attrs={'class':'price-value'}).get_text()
        else:
            continue

        star = item.find('em',attrs={'class':'rating'}) # 평점
        if star:
            star = item.find('em',attrs={'class':'rating'}).get_text() 
        else:
            continue

        review = item.find('span',attrs={'class':'rating-total-count'}) # 리뷰 수
        if review:
            review = item.find('span',attrs={'class':'rating-total-count'}).get_text() # ex) (36)
            review = review[1:-1]
        else:
            continue
        
        link = item.find('a', attrs={'class':'search-product-link'})['href']
        
        #리뷰 100개 이상, 평점 4.8 이상 제품만 표시
        if float(star) >= 4.8 and float(review) >= 100:
            print(f"제품명 : {name}")
            print(f'가격 : {price}')
            print(f'평점 : {star}, ({review})개')
            print(f'바로가기 : https://www.coupang.com{link}')
            print('-'*100)