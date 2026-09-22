# # 연산자 : 프로그램에서 값을 계산하거나 변수에 대해 연산을 수행하는 기호
#
# # 산술 연산자
# # 숫자형 데이터 사이에서 기본적인 사칙연산 정수는 정수형끼리 실수형은 실수형으로 결과를 반환
# # 문자열에 대해서도 일부 산술 연산은 가능합니다
# i = 10
# j = 4
# print(i + j)   # 덧셈 : 14
# print(i - j)   # 뺄셈 : 6
# print(i * j)   # 곱셈 : 40
# print(i / j)   # 나눗셈 : 2.5
# print(i % j)   # 나머지 : 2
# print(i // j)  # 몫 : 2
# print(i ** 4)  # 제곱 : 10 * 10 * 10 * 10
#
# #문자열에 대한 연산
# text = "Python"
# print(text + " Programming")  # 문자열 연결
# print(text * 3)               # 문자열 반복
#
# # 응용 예제
# tax_rate = 0.10
# income = input("당신의 수입(급여) : ")
# if income.isdigit():
#     income = int(income)
#     print(f"당신이 내야할 세금은 {income * tax_rate:.2f}원입니다.")
# else:
#     print("잘못 입력된 값 입니다.")
#
# # 대입 연산자
# # 변수에 값을 할당하거나, 복합적으로 값을 갱신할 때 사용됩니다.
# # =, +=, -=, *=, /=, //=, %=
# num1 = 10
# num1 += 2    # num1 = num1 + 2
# print(num1)  # 12
# num1 -= 2
# print(num1)  # 10
# num1 *= 2
# print(num1)  # 20
# num1 //= 2
# print(num1)  # 10
# num1 %= 2
# print(num1)  # 0
#
# # 비교 연산자
# # 두개의 값을 비교하여 조건이 참인지 거짓인지 판별 합니다.
# # == 같다 , > 크다, != 같지 않다,  <= 작거나 같다, < 작다, >= 크거나 같다.
# a = 10
# b = 20
# print(a > b)
# print(a < b)
# print(a == b)
# print(a != b)
# print(a >= b)
# print(a <= b)
#
# # 논리 연산자
# # 조건을 비교하여 참(true) 과 거짓(false)을 반환
# # and(둘다 참이면) or (둘중 하나) not(조건의 결과를 반전)
# x = 10
# y = 20
#
# print(x > 5 and y > 15)  # True
# print(x > 15 or y > 15)  # True
# print(not(x > 15))       # True
#
# # 삼항 연산자 (조건문)
# num = 100
# flag = "짝수" if num % 2 == 0 else "홀수"
# print(flag)
#
# age=18
# is_adult = "성인" if age> 19 else "미성년"
# print(is_adult)
#
# # 윤년 계산하기 (조건)
# # 연도가 4로 나뉘어 떨어짐  /4
# # 100으로 나누어 떨어지면 연도는 윤년이 아니다. /100
# # 400으로 나누어 떨어지면 윤년이다 /400
# yearSun=365.25
# year = int(input("년도를 입력해주세요: "))
# if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0): #간결
#     print(f'{year}년은 윤년입니다.')
# else:
#     print(f'{year}년은 윤년이 아닙니다.')
#
# # 논리적 코드
# year = int(input("년도를 입력해주세요: "))
#
# if year % 400 ==0: # 400의 배수면 윤
#     print(f'{year}년은 윤년입니다.')
#
# elif year % 100 ==0: # 100의 배수면 평년
#     print(f'{year}년은 윤년이 아닙니다.')
#
# elif year % 4 ==0: #4의 배수면 윤
#     print(f'{year}년은 윤년입니다.')
#
# else: # 평년
#     print(f'{year}년은 윤년이 아닙니다.')
#
#
# # 연산자 우선 순위
# # 1. 소괄호 ( )
# # 2. 거듭 제곱 **
# # 3. 곱셈, 나눗셈, 나머지, 몫 *, /, %, //
# # 4. 덧셈, 뺄셈 +, -
# # 5. 비교 연산자 <, >, <=, >=, ==, !=
# # 6. 논리 연산자 not, and, or
#
# # result = 5 + 2 * 3
# # print(result)  # 11 (곱셈이 먼저 수행)
# #
# # result = (5 + 2) * 3
# # print(result)  # 21 (소괄호가 우선)
#
# # 100의 자리 정수를 입력 받아  100의 자리, 10의 자리, 1의 자리 나누어 담기
# # 789를 넣으면 789//100 = 7 (789//10)%10 = 8  789%10 = 9
# number= int(input("숫자를 입력하세요: "))
# num1 = number//100
# num2 = (number//10)%10
# num3 = number%10
# print(f'입력: {number} → {sum([num1,num2,num3])}')