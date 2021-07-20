'''
regular expression(정규식): 정해진 형태의 식
'''
#4자리 문자 ex) abcd, desk, book,...
#4자리 문자 중 3자리 밖에 모르는 상황
#ca?e
#caae, cabe, cace,... 하나씩 조사하기에는 일이 너무 많음 -> 정규식 사용

import re
p = re.compile("ca.e") 

# . (ca.e): 하나의 문자를 의미 = ?(물음표)
# ^ (^de): 문자열의 시작을 의미 ex) desk, destination,... (O) | fade (X)
# $ (se$): 문자열의 끝을 의미 ex) case, base,.. (O) | face (X) 

#print(m.group()) #매칭되지 않으면 에러가 발생

def print_match(m):
    if m: #매칭되는 경우만 실행
        print('m.group():',m.group()) #일치하는 문자열 반환
        print('m.string:',m.string) #입력받은 문자열 반환
        print('m.start():', m.start())  #일치하는 문자열의 시작 index
        print('m.end():', m.end())     #일치하는 문자열의 끝 index
        print('m.span()', m.span())   #일치하는 문자열의 시작과 끝 index
    else:
        print('매칭되지 않음')

m1 = p.match("careless") # 주어진 문자열의 처음부터 일치하는지 여부를 확인. 
print_match(m1)          # 그렇기에 일치하는 문자열의 뒷부분에 다른게 있어도 상관 X ex) careless -> 올바르게 인식

print()

m2 = p.search("good care") # search: 주어진 문자열 중에 일치하는게 있는지 확인.
print_match(m2)

print()

m3 = p.findall('careless cafe') # indall: 일치하는 모든 것을 리스트 형태로 반환
print(m3)

'''
정리:
1. p = re.compile("원하는 형태")
2. m = p.match("비교할 문자열"): 주어진 문자열의 처음부터 일치하는지 확인
3. m = p.search("비교할 문자열"): 주어진 문자열 중에 일치하는게 있는지 확인
4. lst = p.findall("비교할 문자열"): 일치하는 모든 것을 '리스트' 형태로 반환

원하는 형태: 정규식
. : 하나의 문자를 의미
^ : 문자열의 시작 의미
$ : 문자열의 끝 의미
'''
