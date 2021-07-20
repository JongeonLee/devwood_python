import requests
url = 'https://google.com'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
#User-Agent를 설정함으로써 접근 권한 이 없던 사이트에서도 html 정보를 불러올 수 있음
res = requests.get(url, headers= headers)
res.raise_for_status()

with open('mygoogle.html','w', encoding='utf-8') as f:
    f.write(res.text)