from bs4 import BeautifulSoup

# BeautifulSoup
#    파이썬에서 사용할 수 있는 웹 데이터 크롤링 라이브러리

htmlEx = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>크롤링 연습</title>
</head>
<body>
    <h1>h1 태그</h1>
    <h2>h2 TAG</h2>
    <p><b>BeautifulSoup</b></p>
    
    <p>Python에서 Crawling할 때 유용하게 사용할 수 있는 Libaray
        <a href="https://www.google.com">구글</a>
        <a href="https://www.naver.com">네이버</a>
        <a href="https://www.youtube.com">유튜브</a>
    </p>
    <p>How to use bs4</p>
</body>
</html>
"""

# bs4 초기화
# html.parser : HTML 문법 규칙에 따른 문자열, 해당 문법을 바탕으로 그 단어의 의미나 구조를 분석하는 프로그램
soup = BeautifulSoup(htmlEx,'html.parser')

print(soup)

# 코드를 예쁘게 정리하기 -prettify()
print(soup.prettify())

# title 부분 찾기
title = soup.html.head.title
print(title) # title의 태그 까지 전부
print(title.string) # title 태그의 text만
print(title.text)
print(title.getText())
print('-'*25)

# h1 태그 가져오기
h1 = soup.html.body.h1
print(h1)
print(h1.text)
print('-'*25)

# p 태그 가져오기
p = soup.html.body.p
print(p)
print(p.string)
print('-'*25)

# next_sibling : 동일한 레벨 상의 다음 요소를 불러올 수 있는 기능
#    <=> previous_sibling : 위의 next의 반대임.
# 태그와 태그 사이에 개행이 있는 경우, 엔터 처리로 취급함.
#    > 요소로 인식함
p2 = p.next_sibling.next_sibling
print(p2,'\n')
print(p2.text)
