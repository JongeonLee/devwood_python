import requests
from bs4 import BeautifulSoup
#동적 페이지(ex. 스크롤을 내림에 따라 컨텐츠가 계속 늘어남)

url = 'https://play.google.com/store/movies/top'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accet-Language':'ko-KR,ko'
}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

movies = soup.find_all('div', attrs ={'class':'ImZGtf mpg5gc'})
for movie in movies:
    title = movie.find('div', attrs={'class':'WsMG1c nnK0zc'}).get_text()
    print(title)
    
# with open('movie.html', 'w', encoding='utf-8') as f:
#     #f.write(res.text)
#     f.write(soup.prettify()) # html 문서를 예쁘게 출력