# 검색어 입력시, 관련 뉴스 내용의 제목들을 출력

from urllib.parse import quote
import requests
from bs4 import BeautifulSoup

# https://search.daum.net/search?w=news&nil_search=btn&DA=NTB&enc=utf8&cluster=y&cluster_page=1&q=

q = quote(input("검색어 : "))
# requests : 간편하게 HTTP 요청을 하기위해 사용하는 모듈 library

for i in range(1,6):

    url = f"https://search.daum.net/search?w=news&nil_search=btn&DA=NTB&enc=utf8&cluster=y&cluster_page=1&q={q}&p={i}"
    response = requests.get(url)
    
    if response.status_code == 200:           
            
        html = response.text
        soup = BeautifulSoup(html,'html.parser') 
        ul = soup.select_one('ul.c-list-basic')
    
        # #dnsColl > div:nth-child(1) > ul > li:nth-child(1) > div.c-item-content > div.item-bundle-mid > div.item-title > strong
        title = ul.select('li > div.c-item-content > div.item-bundle-mid > div > strong > a')  
        print('-'*30)
        print(f'{i}번째 페이지')
        for t in title:           
            print(t.getText())                
        
    
    else:
        print(response.status_code)
        
print('-'*30)