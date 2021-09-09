import requests
import re
from bs4 import BeautifulSoup

url = 'https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor='
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

items = soup.find_all('li', attrs={'class':re.compile('^search-product')}) 
#'search-product'로 시작하는 모든 li 태그들을 가져와줌
#ex) 'search-product search-product__ad-badge'도 포함

#print(items[1].find('div',attrs={'class':'name'}).get_text())

for item in items:
    #광고 상품 제외
    ad_badge = item.find('span',attrs={'class':'ad-badge-text'})
    if ad_badge:
        print('  < 광고 상품 제외>')
        continue

    name = item.find('div',attrs={'class':'name'}).get_text() # 제품명
    # 애플 제품 제외
    if 'Apple' in name:
        print('  <애플 상품 제외>')
        continue

    price = item.find('strong',attrs={'class':'price-value'}).get_text() # 가격

    star = item.find('em',attrs={'class':'rating'}) # 평점
    if star: # 평점이 없는 제품 방지를 위해
        star = item.find('em',attrs={'class':'rating'}).get_text() 
    else:
        star = "평점 없음"
        print('<  평점 없는 상품 제외>')
        continue

    review = item.find('span',attrs={'class':'rating-total-count'}) # 리뷰 수
    if review: # 리뷰가 없는 제품 방지를 위해
        review = item.find('span',attrs={'class':'rating-total-count'}).get_text() # ex) (36)
        review = review[1:-1] # 괄호 제거
    else:
        review = "리뷰 없음"
        print('  <리뷰 없는 상품 제외>')
        continue
    
    #리뷰 100개 이상, 평점 4.8 이상 제품만 표시
    if float(star) >= 4.8 and float(review) >= 100:
        print(name, price, star, review)