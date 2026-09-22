# 내장함수 : 파이썬에서 기본 제공, import 없이 사용
"""
- `input()`: 사용자로부터 입력을 받는 함수입니다.
- `int()`: 정수로 형변환을 해주는 함수입니다.
- `str()`: 문자열로 형변환을 해주는 함수입니다.
- `range()`: 순차적인 정수를 생성하는 함수입니다.
- `len()`: 컨테이너(문자열, 리스트 등)의 길이를 반환하는 함수입니다.
- `print()`: 값을 출력하는 함수입니다.
- `sum()`: 숫자들의 합을 계산하는 함수입니다.
- `sorted()`: 순서가 있는 자료형을 정렬하는 함수입니다.
- `max()`, `min()`: 최댓값과 최솟값을 반환하는 함수입니다.
"""
import time

ls = [32, 45, 11 ,57 ,50, 89, 90] # 연속된 값을 저장할때
print(f"합계: {sum(ls)}")
print(f"리스트: {ls}")
print(f"평균: {sum(ls)/len(ls)}")
print(f"f최대값: {max(ls)}")
print(f"f최소값: {min(ls)}")
print(f"몫과 나머지:{divmod(sum(ls), len(ls))}")
print(f"오름차순: {sorted(ls)}")
print(f"내림차순: {sorted(ls, reverse=True)}")

#이름과 5과목의 정석을 입력 받아 이름, 총점, 평균, 최대값, 최소값 구하기
# name = input("이름:")
# sc_list = list(map(int, input("5과목: ").split()))

score_list = [70,88,45,30,99]
subject_list = ["국어","수학","영어","역사","과학"]
name_list = ["철수","영희","유리","하늘","주석"]

print(f"이름:{name_list}")
print(f"과목:{subject_list}")
print(f"총점: {sum(score_list)}")
print(f"평균: {sum(score_list)/len(score_list)}")
print(f"f최대값: {max(score_list)}")
print(f"f최소값: {min(score_list)}")

# 외장함수 : 파이썬에서 기본 제공, 단 import 해서 사용
import  random
# from random import randint

    # randint(m,n)
# - 지정한 범위 안의 임의의 수를 구하는 함수
# - m~n
for i in range(20):
    print(f"{random.randint(1,100)}", end=", " ) # 1 ~ 100 사이의 임의의 값
print()

# randrange (m,n,p)
for i in range(20):
    print(f"{random.randrange(1,100, 2)}", end=", " ) # 1에서 100미만
print("\n")

# 무인도 탈출 게임
# 두개의 주사위를 굴려 같은 값이 나오면 "무인도를 탈출 했습니다. 탈출 시도 횟수, 두개의 주사위 값"

attempt = 0
while True:
    dice1 = random.randint(1,50)
    dice2 = random.randint(1, 50)
    attempt += 1
    if dice1 == dice2:
        print(f"무인도를 탈출했습니다. 탈출 시도 횟수: {attempt}회, 두 개의 주사위 값: {dice1}, {dice2}")
        break

# 로또 번호 생성
lotto = []
while True:
    rotto_numer =random.randint(1,45)
    if rotto_numer not in lotto: # 생성된 난수가 로또 리스트에 포함되어 있지 않으면
        lotto.append(rotto_numer) # 리스트의 마지막에 값 추가
    if len(lotto) == 6:            # 중복되지 않은 번호가 6개가 되면 반복문 탈출
        break

print(f"번호는: {lotto}")

# 날짜 및 시간
from datetime import datetime

datetime.today()            # 현재 날짜 가져오기
datetime.today().year       # 현재 연도 가져오기
datetime.today().month      # 현재 월 가져오기
datetime.today().day        # 현재 일 가져오기
datetime.today().hour       # 현재 시간 가져오기

print(f"월:{datetime.today().month}")
print(f"일:{datetime.today().day}")
print(f"시간:{datetime.today().hour}")
print(f"분:{datetime.today().minute}")
print(f"초:{datetime.today().second}")

# 오늘은 2024년 10월12일 토요일 10시31분 입니다.
# 현재 시간 가져 오기
# %Y : 4자리 연도
# %m : 2자리 월
# %d : 2자리 일
# %A : 요일 표시
# %H : 24시간 형식의 시간
# %M : 분 표시
now = datetime.now()
#원하는 출력 형식 만들기
formatted = now.strftime("오늘은 %Y년 %m월%d일 %a %H시%M분 입니다.")
print(formatted)

# 생일 일수 계산하기
birthday = datetime(year=1997,month=10 , day=18)
print(f"생일:{birthday.day}")
print(f"생일까지 남은 일수:{datetime.today().day +birthday.day } ")
print()

# 요일별 인사말 출력
day_of_week = datetime.today().weekday()
# day_of_week = today().weekday()
if 0 <= day_of_week < 4:
    print(f"월~금:오늘은 평일입니다. 힘내세요!")
else:
    print("토,일: 오늘은 주말입니다. 푹 쉬세요!.")
print()


# 현재 시단대별 인사말 만들기
# 06~11시 : 좋은 아침
# 12~17시 : 좋은 오후
# 18~22시 : 좋은 저녁
# 그 외 : 늦은 밤
hour = datetime.today().hour
if hour == 6 <= hour <= 11:
    print("좋은 아침입니다.")
elif hour == 12 <= hour <= 17:
    print("좋은 오후입니다.")
elif hour == 18 <= hour <= 22:
    print("좋은 저녁입니다.")
else:
    print("늦은 밤이네요. 얼른 주무세요")

# 원하는 형식으로 파일명 생성
# strftime 활용해서 로그 파일명 만들어 보기
# 예: "backup_20261014_1530.txt"
form = now.strftime("backup_%Y%m%d_%H%M.txt")
print(form)

# 달력 가져오기 (필요없음)
# import calendar
# print(calendar.calendar(2023)) # 달력 전체 출력
# print(calendar.calendar(2023, m=4)) # 달력 전체 출력 / 조건:4개 열로 표시
# print(calendar.month(2023, 9)) # 지정한 연도의 특정 월 표시 (9월만)
# print(calendar.monthrange(2023, 9)) # 시작 요일과 일수 반환

# math (수학 모듈)
import math
print(math.sin(100))
print(math.cos(100))
print(math.tan(100))
print(math.log(10))
print(math.ceil(100.01)) # 소수점 이하를 올림
print(math.floor(100.01)) # 소수점 이하를 내림

from simple_colors import *
print(green('hello'))
print(yellow('hello', 'bold'))
print(red('hello', 'bold',))


#
choices = ["가위","바위","보"]
user = int(input("가위(0) 바위(1) 보(2) 중 선택: "))
cnt = 0
while True:
    computer = random.randint(0,2) # 가위(0) / 바위(1) / 보(2)
    cnt += 1
    if computer == user:
        print("무승부! 다시 도전합니다....")
        continue
    if (user - computer) % 3 == 1:
        print(f"승리하였습니다. 총 {cnt}번 만에 승부가 났습니다.")
        break
    else:
        print(f"패배하였습니다. 총 {cnt}번 만에 승부가 났습니다.")
        break


now = datetime.today()
login = now.strftime("%Y년 %m월 %d일 / %H시 %M분 %S초")

first_login = datetime.today() # 시점 1 저장
time.sleep(20) # 기다림 5초
second_login =datetime.today() # 시점 2 저장

total = (second_login - first_login).total_seconds()
sec_floor = math.floor(total)

print(f"로그인 시각 : {login}  → 2번째 접속까지 경과 시간: {sec_floor}초")