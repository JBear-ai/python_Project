# 정수 출력 int
print(30)
age = 23

print(f"나이: {age}") # f-string 방식
print("나이: " + str(age)) # str부여

#실수 출력 float
avg = 76.6667
print(f"성적: {avg:.2f}")
print(float(avg))

# 문자열 출력 string
name = "네버다이"
print("이름: " + name)
print(f"이름: {name}")

#리스트 출력 list
# 파이썬은 배열이업슴 리스트로 연속된 데이터를 관리
score = [99,87,77] # 인덱스 순서 0 1 2
print(f"성적: {score[1]}") # 87점만 출력

#여러 줄 출력
print("""에이이이이이이
아아아넝노ㅓㅏㅍ차ㅓ포
""")

#줄바꿈 문자 확인 (Escape) \n: new line
print("아에이오우우우", end=' ')
print("보우하사 우리나라 만세")

# \t \"
print("apple\tbanana\torange")
print("apple\tbanana\torange")

# 제어 문자, Escape sequence  : \n,\t,\\,\r,\b
# \n: 다음 주로 이동하며 개행이라고 부름
# \t: 탭 문자, 키보드의 Tab 키와 같으며 여러 칸을 띄움
# \\: \ 문자 자체를 출력할 때는 \를 두번 써야하고 다른걸 출력할때 \"
print("보우하사\t우리나라\n 만\b세")
print("보우하사 \n우리나라 \\만세")

print("안녕하세요. \"장원영\"님 환영합니다.") # \"
print("딸기\r바나나\r키위") # \r을 많이 쓴다??? 동기화

print("파이썬")
print("파"+"이"+"썬")
print("파""이""썬")
print("파","이","썬")

# end : 문자열을 출력 하고 난 다음의 동작, 기본값이 줄바꿈 defaul=(\n)
# sep : 문자열 사이에서 (,)콤마를 만나면 동작, 기본값이 스페이스


print("life is shot,", "you need python")
print("life is shot","\n")

print("you", "need", "python", sep="\n")

# 정렬과 포맷 지정
# < : 왼쪽 정렬
# > : 오른쪽 정렬 (기본값)
# ^ : 중앙 정렬

num1 = 10
num2 = 100
num3 = 1000
print(f" num1: {num1}\n num2: {num2}\n num3: {num3}")

print(f"|{num1:5}|") # 공간을 주니 정렬이 오른쪽으로 정렬로 잡혀있다  >
print(f"|{num2:<5}|")
print(f"|{num3:^8}|") # 중간 정렬을 확인하기 위해 칸을 늘림

# 소수점 이하 출력
PI = 3.141592
print(f"PI = {PI:.2f}")

# 다양한 출력 스타일
name = "강문석"
age = 28
gender = 'M'
job = '개발자'
addr = '충남 천안시 동남구'

# 파이썬 스타일2, 가장 최근에 추가된 (f-string), 방식 3.6 이후
# f와 {}로 사용합니다.
print("=========== 파이썬 스타일 2번째 ===========")
print(f'이름: {name}')
print(f'나이: {age} ')
print(f'성별: {gender} ')
print(f'직업: {job}')
print(f'주소: {addr}')


#자바 스타일
print("====== 자바 스타일 ======")
print("이름 : " + name)
print("나이 : " + str(age))
print("성별 : " + gender)
print("직업 : " + job)
print("주소 : " + addr)

# 1. \n, \t 를 사용하여 아래와 같은 형태로 자기소개를 한 줄의 print 출력
# 이름 : 김민준
# 직업 : 백엔드 개발자
name2 = '김민준'
job2 = '백엔드 개발자'
print(f"\n이름 : {name2}")
print(f"직업 : {job2}")

# 2. 따옴표 출력하기
print('\n\"오늘도 좋은 하루 되세요!\"라고 인사했습니다.')

#3. \r 로 커서 이동 확인하기
# -사과 바나나 키위를 연속 입력해서 키위만 나오기
print("\n사과\r바나나\r키위")

#4. "010", "1234", "5678" 새 문자열을 sep="-" 옵션을 이용해 붙여서 출력
phone1 = "010"
phone2 = "1234"
phone3 = "5678"
# print(f'{phone1}"\"{phone2}","{phone3}', sep="-")
print(phone1,phone2,phone3,sep='-')

# 5. 아래 세 개의 print()문을 각각 작성하되, end 옵션을 이용해서 한줄로
print("\n결과: ",end='')
print("파이썬은",end='')
print(" 재미있다.\n")

#6. 두가지 스타일로 자기 소개 출력하기
# f-string
name3 = "김철수"
age3 = 20
job3 = '학생'
print(f'이름: {name3}')
print(f'나이: {age3} ')
print(f'직업: {job3}')


print("\n이름 : " + name3)
print("나이 : " + str(age3))
print("직업 : " + job3)

#7. 정렬로 표 만들기
num4 = 7
num5 = 42
num6 = 365

print(f"\n|{num4:^6}|")
print(f"|{num5:^6}|")
print(f"|{num6:^6}|\n")

# 8. 원의 반지름 r=5 이용해 원의 넓이 (3.1459*r*r)를 구한 뒤, 폭 10칸, 오른쪽 정렬, 소수점 둘째 자리 출력
r=5
PI2=3.1459
PI_R = (PI2 * r * r)
print(PI_R)
print(f"{PI_R:2f}")
print(f"넓이 값: {PI_R:10.2f}") # {변수 : 정렬,소수점}
# print(f"넓이 값: {(PI2*r*r):.f2}")
