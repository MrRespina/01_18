-- 학생 : 이름, 생일, 몇 강의장, 중간고사점수 , 기말고사점수

-- 강의장 : 몇 강의장 , 강의장 위치
-- 1 강의장 : 5층 복도 오른쪽
-- 2 강의장 : 5층 복도 왼쪽 끝
-- 3 강의장 : 5층 복도 왼쪽 첫 번째
-- 4 강의장 : 6층 왼쪽
-- 5 강의장 : 6층 오른쪽

CREATE TABLE students(
	s_name varchar(10 char) primary key,
	s_birth varchar(12 char) not null,
	s_classroom varchar(10 char) not null,
	s_midtest number(3) not null,
	s_finaltest number(3) not null
)

CREATE TABLE classrooms(
	c_name varchar(7 char) primary key,
	c_info varchar(20 char) not null
)

INSERT INTO classrooms VALUES('1 강의장','5층 복도 오른쪽')
INSERT INTO classrooms VALUES('2 강의장','5층 복도 왼쪽 끝')
INSERT INTO classrooms VALUES('3 강의장','5층 복도 왼쪽 첫 번째')
INSERT INTO classrooms VALUES('4 강의장','6층 왼쪽')
INSERT INTO classrooms VALUES('5 강의장','6층 오른쪽')

SELECT * FROM classrooms

DROP TABLE students

CREATE SEQUENCE students_seq

SELECT * FROM students

DELETE FROM students WHERE s_name='김영민'