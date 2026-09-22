# 100의 자리 정수를 입력 받아  100의 자리, 10의 자리, 1의 자리 나누어 담기
# 789를 넣으면 789//100 = 7 (789//10)%10 = 8  789%10 = 9
# number= int(input("숫자를 입력하세요: "))
# num1 = number//100
# num2 = (number//10)%10
# num3 = number%10
# print(f'입력: {number} → {sum([num1,num2,num3])}')

# 1. 대입 연산자 실습
num=50
print(num)
num+=20
print(num)
num*=3
print(num)
num%=7
print(num)
num-=2
print(num)

# 2. 논리연산자로 범위 판별
# 사용자에게 점수 0~100
# score = int(input("점수를 입력하세요: "))
# if score >=60 and score <80:
#     print("보통이 아니군요?")
# else:
#     print("보통 아님 불합격 ")
#
#
# # 3.
# a=int(input("첫 번째 수 입력: "))
# b=int(input("두 번째 수 입력: "))
# if a==b:
#     print(" 두 수의 값이 같군요")
# else:
#     max_num = a if a>b else b
#     print(f"두 수의 값은 다릅니다. {max_num}")

# flag = "짝수" if num % 2 == 0 else "홀수"
# print(flag)

# 4.
star = "*"
print(star*10 +"학생 명단"+star*10 )
print("1. 홍길동")
print("2. 김철수")
print(star*25 )

# 5. 사용자에게 태어난 연도 (예:2000)를 입력받아 다음을 계산하는 프로그램 작성하기
# 현재 연도2026 기준으로 만 나이를 계산 합니다 (2026- 태어난 연도 )
# 계산된 나이가 짝수이지 홀수인지 구별하기 위해 나머지 연산자를 씀
#
# year_birth =int(input("태어난 연도를 입력하세요(예: 2000): "))
#
# from datetime import  datetime
# current_year = datetime.now().year
#
# age = int(current_year - year_birth)
#
# # print(age) 잘 출력이 되는지 확인용
# if age % 2 == 0:
#     print(f"계산된 나이는 {age}세이며 짝수 입니다." )
# else:
#     print(f"계산된 나이는 {age}세이며 홀수 입니다. ")
