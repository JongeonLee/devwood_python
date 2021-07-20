import requests
res= requests.get('https://google.com')
print('응답코드:', res.status_code) # 200이면 정상 [ex) 403: 웹 페이지에 접근할 권한이 없는 것]

# if res.status_code == requests.codes.ok: #->200
#     print("정상입니다.")
# else:
#     print('현재 문제가 있습니다. [에러코드:',res.status_code,']')

res.raise_for_status() #문제가 있을 시 에러 문자를 보내고 프로그램을 종료시킴
print("웹 스크래핑을 진행합니다")

print(len(res.text)) #웹페이지의 가져옴

with open('mygoogle.html','w', encoding='utf-8') as f:
    f.write(res.text) #mygoogle.html을 default browser로 열면 구글 홈페이지 비슷한 형태로 나옴