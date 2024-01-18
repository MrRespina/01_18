'''
Created on 2024. 1. 18.

@author: sdedu
'''
# xml, json > 대기업들이 제공하는 데이터, 공공기관에서 제공하는 데이터
#    만약, 찾는 데이터가 대기업, 공공기관에서 제공이 안 된다면?
#    

# 웹 크롤링(Web Crawling) / 웹 스크래핑(Web Scraping)
#    : 웹 페이지에 널려있는 데이터들을 프로그래밍적으로 추출하는 것!

# 웹은 개발자들이 어떠한 정형화 되어있는 형태로 관리 > 규칙이 생기기 마련
#    > 그 규칙을 분석해서 원하는 정보들만 뽑아내는 작업

# 웹 크롤링 자체가 불법은 아님. 하지만 ... > 불법으로 간주되는 경우도 있다.
#    > 조심해서 사용해야 함.

# url - 이미지 : https://i.kfs.io/album/global/216934121,0v1/fit/500x500.jpg

import urllib.request as req

img = "https://i.kfs.io/album/global/216934121,0v1/fit/500x500.jpg"
html = "https://www.google.com"

dirc = "C:/Users/sdedu/Desktop/Dev/prac/crawling/"

path1 = "siu.jpg"
path2 = "google.html"

# 예외 처리
try:
    # urlretrieve() : 다운 받을 파일 및 저장 정보를 return 해줌.
    f1,h1 = req.urlretrieve(img,dirc+path1)
    f2,h2 = req.urlretrieve(html,dirc+path2)
except Exception as e:
    print(e)
    print('실패!')
else:
    # 정상적으로 작동되었을 경우.
    # Header 정보를 출력 : 개발자 도구 > Network > Headers
    print(h1)
    print('-'*40)
    print(h2)
    
    # 다운로드 파일 정보
    print(f"이미지 정보 : {f1}")
    print(f"파일 정보 : {f2}")
    print('성공!')