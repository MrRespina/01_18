
from urllib.parse import quote
import requests
from bs4 import BeautifulSoup

# https://kin.naver.com/search/list.naver?query=

q = quote(input("검색어 : "))

url = f"https://kin.naver.com/search/list.naver?query={q}"
# requests : 간편하게 HTTP 요청을 하기위해 사용하는 모듈 library
response = requests.get(url)

if response.status_code == 200:
    html = response.text
    # print(html)
    
    soup = BeautifulSoup(html,'html.parser')
    # select_one() 을 사용할 경우 : 문서의 처음부터 찾게 되며,
    #        가장 처음에 만난 해당 selector를 호출
    
    ul = soup.select_one('ul.basic1')
    # print(ul)
    
    # select()를 사용할 경우 : 해당하는 selector들의 모든 내용이 List에 담김
    # #s_content > div.section > ul > li:nth-child(1) > dl > dt > a
    # > : 그 하위에 있는 selector들 전부 다 라는 뜻
    
    titles = ul.select('li > dl > dt > a')
    print(titles)
    
    for t in titles:
        print(t.getText())
        
else:
    print(response.status_code)