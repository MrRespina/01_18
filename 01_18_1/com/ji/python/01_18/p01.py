'''
Created on 2024. 1. 18.

@author: sdedu
'''

# 메뉴 만들기 (함수)
# 1. 학생 등록 / 2. 강의장 조회 / 3. 학생 조회
# 4. 학생 정보를 파일로 내보내기
# 0. 종료

# 강의장 조회 : 1 강의장 - 5층 복도 오른쪽
# 학생 조회 : 이름, 생년월일(연-월-일)(요일),나이,몇 강의장,중간,기말,평균점수

# 파일 내보내기 : 학생의 전체 정보 csv 파일로 출력.

from cx_Oracle import connect
import datetime as dt

def getName():
    
    s_name = input('학생의 이름을 입력해주세요 : ')
    return s_name

def getBirth():
    
    s_birth = input('학생의 생년월일을 입력해주세요 ex)1999-05-30 : ')
    birth = s_birth.split("-",2)
    
    try:
        if birth[1] not in ['01','02','03','04','05','06','07','08','09','10','11','12']:
            print("월은 01~12 사이의 숫자를 입력해주세요!")
            getBirth()
        elif birth[2] not in ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']:
            print("일은 01~31 사이의 숫자를 입력해주세요!")
            getBirth()
        else:      
            return s_birth
    except Exception:
        print('생년월일을 정확히 입력해주세요!\nex) 1999-11-25')
        getBirth()
        
def getClassroom():
    
    try:
        s_classroom = int(input('강의장의 번호를 입력해주세요 (1,2,3,4,5) : '))
        if s_classroom not in [1,2,3,4,5]:
            print('강의장의 번호는 1,2,3,4,5 중에서만 입력해주세요!')
        else:
            return s_classroom
    except Exception:
        print('강의장의 번호는 숫자만 입력해주세요!')
        getClassroom()
        
def getMidTest():
    
    try:
        s_midtest = int(input('중간고사 점수를 입력해주세요 : '))
        if (s_midtest > 100) | (s_midtest < 0):
            print('중간고사 점수를 정확히 입력해주세요!(0~100)')
            getMidTest() 
        else:
            return s_midtest
    except Exception:
        print('중간고사 점수를 정수로 입력해주세요!')
        getMidTest()
        
def getFinalTest():
    
    try:
        s_finaltest = int(input('기말고사 점수를 입력해주세요 : '))
        if (s_finaltest > 100) | (s_finaltest < 0):
            print('기말고사 점수를 정확히 입력해주세요!(0~100)')
            getFinalTest() 
        else:
            return s_finaltest
    except Exception:
        print('기말고사 점수를 정수로 입력해주세요!')
        getFinalTest()

def regStudent():
    
    con = connect('respina/sdj7524@localhost:1521/xe')
    
    name = getName()
    print()
    birth = getBirth()
    print()
    classroom = getClassroom() 
    print()
    midtest = getMidTest()
    print()
    finaltest = getFinalTest()

    
    sql  = f"INSERT INTO students VALUES(\'{name}\',\'{birth}\',{classroom},{midtest},{finaltest})" 
    print(sql)
    cur = con.cursor() 
    cur.execute(sql)
    print('')

    if cur.rowcount == 1: # 방금 작업때문에 영향을 받은 행 수가 하나라면
        con.commit() # DB에 실제로 반영시킴.
        print(f'{name} 님 등록 성공')   
        
    elif cur.rowcount == 0:
        print(f'{name} 님은 이미 존재하는 회원 이름입니다!')
        
    con.close()

def showClassrooms():
    
    con = connect('respina/sdj7524@localhost:1521/xe')

    sql = 'SELECT * FROM classrooms'

    cur = con.cursor()
    cur.execute(sql)
    
    print('*'*40)
    for c_name,c_info in cur:
        print(f"강의장 이름 : {c_name}")
        print(f"강의장 위치 : {c_info}")
        print('*'*40)
        
    print('')
    con.close()

def showStudents():
    
    con = connect('respina/sdj7524@localhost:1521/xe')

    sql = 'SELECT * FROM students'

    cur = con.cursor()
    cur.execute(sql)
    
    print('*'*40)
    for s_name,s_birth,s_classroom,s_midtest,s_finaltest in cur:
        print(f"학생 이름 : {s_name}")
        
        to = s_birth.split('-',2)
        da = dt.date(int(to[0]),int(to[1]),int(to[2]))
        day = da.isoweekday()
        
        now = dt.datetime.today()
        age = now.year - int(to[0])
        
        if day == 0:
            day = '월요일'
        elif day == 1:
            day = '화요일'
        elif day == 2:
            day = '수요일'
        elif day == 3:
            day = '목요일'
        elif day == 4:
            day = '금요일'
        elif day == 5:
            day = '토요일'
        else:
            day = '일요일'    
        print(f"학생 생년월일 : {da},{day}")
        print(f"나이 : {age}")
        
        if int(s_classroom) == 1:
            classroom = '1 강의장'
        elif int(s_classroom) == 2:
            classroom = '2 강의장'
        elif int(s_classroom) == 3:
            classroom = '3 강의장'
        elif int(s_classroom) == 4:
            classroom = '4 강의장'
        elif int(s_classroom) == 5:
            classroom = '5 강의장'
        print(f"학생이 속한 강의장 : {classroom}")
        
        print(f"학생의 중간고사 점수 : {s_midtest}")
       
        print(f"학생의 기말고사 점수 : {s_finaltest}")
        
        print('*'*40)
        
    print('')
    
    con.close()

def getStudentsCSV():

    con = connect('respina/sdj7524@localhost:1521/xe')

    file = open("C:\\Users\\sdedu\\Desktop\\Dev\\prac\\students.csv",'w',encoding='UTF-8')

    sql = 'SELECT * FROM students'

    cur = con.cursor()
    cur.execute(sql) # SELECT의 결과가 cur에 Tuple로 들어감.

    for i in cur:
        file.write(f"{i[0]},{i[1]},{i[2]},{i[3]},{i[4]}\n")
        
    print("전체 학생 정보 생성 완료")   
    print()
    
    file.close()
    con.close()


while True:
    
    print('*'*60)
    print('1. 학생 등록 | 2. 강의장 조회 | 3. 학생 조회 | 4. 전체 학생 정보 생성 | 0. 종료')
    try:
        menuPointer = int(input("원하는 메뉴를 입력하세요 : ")) 
        print('')
        if menuPointer not in [1,2,3,4,0]:
            print('정확한 숫자를 입력해주세요!) 1,2,3,4,0\n')
        else:
            if menuPointer == 0:
                break           
            
            elif menuPointer == 1:
                regStudent()
                
            elif menuPointer == 2:
                showClassrooms()
                
            elif menuPointer == 3:
                showStudents()
                
            elif menuPointer == 4:
                getStudentsCSV()
                
    except Exception as e:
        print(e)
        print('')
        print('입력은 정수만 입력해주세요!) 1,2,3,4,0\n')      

