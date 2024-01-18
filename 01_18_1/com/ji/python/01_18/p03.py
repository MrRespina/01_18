'''
Created on 2024. 1. 18.

@author: sdedu
'''
import urllib.request as req
from urllib.error import HTTPError, URLError

img = "https://i.kfs.io/album/global/216934121,0v1/fit/500x500.jpg"
html = "https://www.google.com"

dirc = "C:/Users/sdedu/Desktop/Dev/prac/crawling/"
path1 = "siu2.jpg"
path2 = "google2.html"

pathlist = [dirc+path1,dirc+path2]
urlList = [img,html]

for i,url, in enumerate(urlList):   # enumerate : 인덱스를 확인할 수 있음.
    
    try:
        # web의 수신 정보를 확인
        res = req.urlopen(url)
        
        # 수신받는 내용
        content = res.read()
        print('-'*40)
        
        # 상태정보 중간 확인
        print(f"헤더 정보 : {i,res.info()}")
        print(f"HTTP STATUS : {res.getcode()}")
        print('-'*40)
        
        # 파일 쓰기
        # with : 파일을 열고, 닫는 것을 같이 해주는 역할을 함.(close가 필요하지 않다.)
        with open(pathlist[i],'wb') as f:
            f.write(content)
        
    except HTTPError as e:
        print("HTTPError Code : ",e.code)
        
    except URLError as e:
        print("URLError Code : ",e.code)