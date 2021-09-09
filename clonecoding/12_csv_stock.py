import csv
import requests
from bs4 import BeautifulSoup

filename = '시가총액1-200.csv'
f = open(filename,'w',encoding='utf-8-sig', newline="")
writer = csv.writer(f)

title = 'N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE'.split('\t')
#리스트 형태로 반환
writer.writerow(title)

for page in range(1,5):
    url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=' + str(page)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    data_row = soup.find('table',attrs={'class':'type_2'}).find('tbody').find_all('tr')
    for row in data_row:
        columns = row.find_all('td')
        if len(columns) <= 1: #의미없는 데이터 제거
            continue
        data = [column.get_text().strip() for column in columns] #불필요한 데이터 제거
        #print(data[:-1])
        writer.writerow(data[:-1]) # writerow에 리스트 형태로 입력