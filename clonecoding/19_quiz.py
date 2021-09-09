import requests
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8'
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

todaymax = soup.find('span', attrs={'class':'max'}).get_text()
morning_rainrate = soup.find_all('span', attrs={'class':'rain_rate wet'})[0].get_text()
afternoon_rainrate = soup.find_all('span', attrs={'class':'rain_rate wet'})[1].get_text()
print(morning_rainrate)
