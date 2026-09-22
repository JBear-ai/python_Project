# 입력 Input
# 표준입력: 콘솔로부터 사용자의 입력을 받음
# - 기본적으로 문자열로 반환됨, 다른 데이터형으로 변환할려면 형 변환 함수 사용

#이름 (string), 나이(int), 성별(string), 주소(string), 평균(float) 입력 받아 출력 해보기
"""
name = input("이름을 입력하세요: ")
age = int(input("나이 입력: ")) # 입력값을 받고 그 데이터를 정수형으로 변환 하는 과정이다
gender = input("성별(M/F):  ").upper()
addr = input("주소를 입력하세요: ")
"""
# 국어, 영어 ,수학 성적을 입력 받아, 총점과 평균을 구하기
# kor = int(input("국어 점수: "))
# eng = int(input("영어 점수: "))
# math = int(input("수학 점수: "))
#
#
# score = list(map(int, input("국어 영어 수학: ").split())) # 강사님의 방식
#
#
# score_count = len(score) # 분모의 수가 늘어날지도 모르는 상황에서 변수로 지정
# AVG = sum(score) / len(score)  # sum(국어 영어 수학) / 3(과목이 3개라 늘어나면 값이 변할 예정)
# print(f"총점2: {sum(score)}점") # 내 방식대로 이것저것 해보는거
# print(f"평균2: {AVG:.2f}점")
#
# # 기존에 하던 예제 방식
# sum_score = sum([kor,eng,math])
# avg_score = sum_score/score_count
# print(f'\n총점: {sum_score}점')
# print(f'평균: {avg_score:.2f}')

"""
print(f'\n이름: {name}')
print(f'나이: {age}')
print(f'성별: {'남성' if gender == 'M' else 'F'}') # =는 대입이라 ==사용
print(f'주소: {addr}')
"""


# 시간을 24제로
# 예) 23:56:45 입력 받아 12제로 변환해서 11시 56분 45초로 형태로 출력
"""
hour, minute, sec = input("24시간 시:분:초 > ").split(":")
hour = int(hour)
minute = int(minute)
sec = int(sec)

if hour == 12:
    print(f"오후{hour:02}시{minute:02}분{sec:02}초")
elif hour > 12:
    hour -= 12 # 번역하면 hour = hour -12
    print(f"오후{hour:02}시{minute:02}분{sec:02}초")
else:
    print(f"오전{hour:02}시{minute:02}분{sec:02}초") 
    다음 문제풀이를 위해 다 주석처리 합니다. 필요할때 꺼내 쓰쇼 
"""
# 이름과 주소 입력 " 안내 문구로 이름과 주소를 공백으로 구분해서 한 번에 입력 받기
name,addr = input("[이름,주소를 입력하세요] (예시:김철수,서울): ").split(",")
print(f"이름: {name}\n주소: {addr}")

# 시:분:초 : 14:5:9 형태의 시간을 콜론 기준으로 입력 받아 map(int)정수 변환한 뒤,
# 각 자리를 2자리 폭에 0으로 채워라
# hour, minute, sec = input("24시간 시:분:초 > ").split(":")
# hour = int(hour)
# minute = int(minute)
# sec = int(sec)  데이터타입을 지정을 안하면 일일이 타입을 줘야하니 복잡합니다.

# 편한 방법
hour, minute, sec = map(int, input("시:분:초 > ").split())
print(f"{hour:02}:{minute:02}:{sec:02}")

# "국어 영어 수학 : " 안내 문구로 세 과목 점수를 공백 기준으로 한 번에 입력 받고 평균을 구하라
subjects_score = list(map(int, input("\n국어,영어,수학 점수입력  \n(예시:44 75 80): ").split())) # 점수 입력 받고
subjects_count = len(subjects_score) # 과목 수 구하기
subjects_avg = sum(subjects_score) / subjects_count # 3개의 과목을 합한 값 / 분모(길이로 갯수 지정)

print(f"\n학생의 평균은: {subjects_avg:.2f}")
if subjects_avg > 60:
    print("평균의 60점을 넘어 합격했습니다.")
else:
    print("평균을 넘지 못했습니다. 불합격!")