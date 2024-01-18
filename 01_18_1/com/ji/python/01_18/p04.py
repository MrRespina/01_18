# fake-useragent
# 어떤 브라우저에서는 get, post방식을 날리는 상대방이 컴퓨터인것을 알게 되면,
#    해당 웹에 점속하는 것을 차단하는 경우가 있다. > 내가 컴퓨터가 아니고 '사람인 척'을 하기 위해서 이 라이브러리를 사용한다.

from fake_useragent.fake import UserAgent
import urllib.request as req
from json import loads

# fake header 정보(가상으로 User-agent 랜덤 생성)
# Python으로 정보를 크롤링하지만, 마치 웹브라우저에서 실행하는 것처럼
#    인식하게 만드는 효과!

ua = UserAgent()

'''
print(ua.ie)
print(ua.msie)
print(ua.chrome)
print(ua.safari)
print(ua.random)
'''

# 헤더 선언 : dict(key,value)로
h = {'User-Agent':ua.chrome,'referer':'https://finance.daum.net/'} # referer : 이 경로를 통해서 사용한다

# 다음 금융 요청 URL
url = 'https://finance.daum.net/api/search/ranks?limit=10'

# 요청
res = req.urlopen(req.Request(url,headers=h)).read().decode("UTF-8")

# 응답 데이터 확인
print('res : ',res)

# 응답 데이터 > str 변환
ranking = loads(res)

# 순위, 주식명, 거래가를 콘솔에 출력

for i in ranking['data']:
    print(f"순위 : {i['rank']}")
    print(f"이름 : {i['name']}")
    print(f"거래가 : {i['tradePrice']}")
    print('-'*30)