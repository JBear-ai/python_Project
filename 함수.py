# 함수 (function) 코드의 특정 블록을 하나의 이름으로 묶은것
# 반복적으로 사용해야 하는 코드나 논리적인 작업을 함수로 정의하면, 재사용성, 가독성, 유지보수
# 즉 컴포넌트 역할을 한다
# def 키워드 / 일반적으로 식별자뒤애() 소괄호가 있으면 함수

# def name_card(name, addr, phone):
#     print(f"주소: {addr}")
#     print(f"전하번호: {phone}")
#     print(f"이름: {name}")
#     print("-"*30)
#
# name_card("안유진", "서울시 강남구 역삼동", "010-1234-5678")
# name_card("장원영", "서울시 강남구 삼성동", "010-1234-9999")
# name_card("가을", "서울시 권서구 권성동", "010-1234-1111")

# 매개변수 O, 반환값 X
# 1-1 이름,나이,취미를 매개변수로 받아서 아래 형식으로 출력하는 함수
def intro_card (name, age, hobby):
    print(f"이름: {name}")
    print(f"나이: {age}")
    print(f"취미: {hobby}\n")
intro_card("안철수" ,50, "개발")
intro_card("김철수" ,40, "낚시")
intro_card("고철수" ,30, "스쿠버다이빙")

# 1-2 과목명
def print_score(subject, score):
    print(f"{subject} 점수: {score}점")
print_score("수학", 90)
print_score("과학", 80)
print_score("역사", 70)

# 2-1
def get_max(a,b):
    if a > b:
        return a
    else:
        return b

# 2-2
def math(r):
    return 3.14*(r**2)

# 2-3
def check_even_odd(num):
    if num % 2 == 0:
        print("짝수")
        return True

    else:
        print("홀수")
        return False

# 기본값 인자 : 함수 선언 시 매개 변수에 대한 기본값을 정의
# - 매개변수에 기본값이 저의 되어 있는 경우 함수 호출 시 인자값을 넣지 않으면 기본값 출력
def profile(name, age, job, addr="대한민국"):
    print(f"이름: {name}")
    print(f"나이: {age}")
    print(f"직업: {job}")
    print(f"주소: {addr}\n")

profile("고경수", 57,"무직","대전시")
profile("장원영", 22,"연예인","서울시")
profile("유진영", 23,"무직")
profile("고경수", 57,"가수",)


# 가변 매개 변수
def profile2(name, age, *lang):
    print(f"이름 : {name}, 나이 : {age}", end="\n")

profile2("나희도",18,"Python","java","C","C++","React","Kotlin")
profile2("조세호",38,"Python","java")
profile2("유재석",48,"Python","java","C","C++")

lang = "Python","Java","C","C++","React"

# 실습 문제: 표준 체중 계산기
# 키(cm)와 성별을 입력받아 표준 체중을 계산하는 함수를 작성하시오.

# 함수 이름은 std_weight로 하고, 매개변수는 키(h)와 성별(gender) 두 개를 받는다.
# 표준 체중 공식은 다음과 같다.
# 남성: (키(m))² × 22
# 여성: (키(m))² × 21
# 단, 입력받은 키는 cm 단위이므로 함수 내부에서 m 단위로 변환해야 한다. (h / 100)
# 함수는 계산된 표준 체중 값을 반환(return) 해야 한다. (출력 X)
# input()을 이용해 사용자로부터 키(cm)와 성별을 입력받는다.
# 키는 정수로 변환하여 저장 (int(input(...)))
# 성별은 "남성" 또는 "여성" 문자열로 입력받음
# 함수 호출 결과를 아래 형식으로 출력하시오. (소수점 둘째 자리까지)

# h = int(input("키를 입력하세요: "))
# g = input("성별 입력하세요: ").upper()
#
# def std_weight (height, gender):
#     if gender == "남성" or "m":
#         return (height**2) * 22 # 남성의 체중
#
#     else:
#         return (height**2) * 21 # 여성의 체중 구하기
#
# std_weight(h, g)

def std_weight(h,sex):
    hm = h /100
    if sex == "남성":
        return hm*hm *22
    else:
        return hm*hm *21

# 키를 입력 받음 : cm
height = int(input("키(cm) 입력"))
gender = input("성별(남성 / 여성) ")
weight = std_weight(height,gender)
print(f"키: {height}cm 에 대한 ")


# 소수 판별하기
def is_prime_func(n):
    if_prime = True
    for i in range(2,n):
        if n % i == 0:
            is_prime = False
    return if_prime

n = int(input("정수를 입력: "))
if is_prime_func(n):
    print(f"{n}은 소수 입니다.")
else:
    print(f"{n}은 소수가 아님")


# 소수의 합 구하기
def prime_func(n):
    is_prime = True
    for i in range(2,n):
        if n % i == 0:
            is_prime = False
    if is_prime:
        return n
    else:
        return 0


# 람다: 간단한 함수의 선언과 호출을 하나의 식으로 간략히 표현
# 람다 함수를 이용해 익명의 함수를 만들수 있다
# 람다 함수의 장점은 코드의 간결함, 메모리 절약

def add(a,b):
    return a+b

print(add(1,2))

print(f"{(lambda a, b:a+b)(1,2)}")

def power(n):
    return n*n

out = list(map(lambda x: x*x,))


# - 사용자로부터 좌석번호(index)를 입력받아 예매하는 시스템이다.
# - 예매가 완료되면 해당 좌석 값을 1로 변경한다.
# - 이미 예매가 완료된 좌석은 재구매할 수 없다.
# - 한 좌석당 예매 가격은 12000원이다.
# - 프로그램 종료 후, 해당 영화관의 총 매출액을 출력한다.

# 좌석 개수 리스트 만들기
seat = [0] * 10
PRICE = 12000

# 좌석 출력 함수


# 좌석 선택 함수


# 판매 금액 계산 함수


# 입력 메뉴 구성