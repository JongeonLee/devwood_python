import requests
from bs4 import BeautifulSoup

#서울 날씨
weather_url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8'
res = requests.get(weather_url)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

todaycast = soup.find('p', attrs ={'class':'cast_txt'}).get_text()

todaytemp = soup.find('p', attrs={'class':'info_temperature'}).get_text().replace('도씨', '')
    #replace(a,b) -> a를 b로 바꿔줌
tempmark = soup.find('span', attrs={'class':'tempmark'}).get_text()
todaymin = soup.find('span', attrs={'class':'min'}).get_text()
todaymax = soup.find('span', attrs={'class':'max'}).get_text()

morning_rainrate = soup.find('li',attrs={'class':'date_info today'}).find_all('span', attrs={'class':'rain_rate'})[0].get_text()
afternoon_rainrate = soup.find('li',attrs={'class':'date_info today'}).find_all('span', attrs={'class':'rain_rate'})[1].get_text()

fine = soup.find('dl', attrs={'class':'indicator'}).find_all('dd')[0].get_text()
ultrafine = soup.find('dl', attrs={'class':'indicator'}).find_all('dd')[1].get_text()

print('[오늘의 날씨]')
print(todaycast.strip())
print('현재 {} (최저{} 최고{})'.format(todaytemp,todaymin,todaymax))
print('오전 {} / 오후 {}'.format(morning_rainrate.strip(),afternoon_rainrate.strip()))
print()
print('미세먼지',fine)
print('초미세먼지', ultrafine)
print()


#네이버 뉴스 헤드라인

#네이버 IT 뉴스 

#해커스 회화