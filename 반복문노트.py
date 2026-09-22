
name = input("이름을 입력하세요: ")
while True:
    age = int(input("나이를 입력하세요: "))
    if 1 <= age <=199:
        break
    else:
        print("입력을 다시 해주세요.")

while True:
    gender = input("성별을 입력하세요.(M/F) ").upper()
    if gender == "M" or gender == "F":
        # if gender == "M":
        #     print({gender})
        # else:
        #     print({gender})
        break
    else:
        print("다시 입력 해주세요 (M/F)")

while True:
    jobs = int(input("직업 입력 (1:학생, 2:회사원, 3:주부, 4:무직): "))
    if jobs == 1:
        jobs = "학생"
        break
    elif jobs == 2:
        jobs = "회사원"
    elif jobs == 3:
        jobs = "주부"
        break
    elif jobs == 4:
        jobs = "무직"
        break
    else:
        print("다시 입력 해주세요. ")

print(f"\n당신의 이름은{name}입니다. \n나이는 {age}세이며, 성별은 {gender} 입니다. \n당신의 직업은 {jobs}입니다.")



# while 문
# for i in range(초기값, 최종값, 증감값)
# for e in sequnce

# n=int(input("정수 입력: "))
# total = 0
#
# while n > 0:
#     total += n
#     n -= 1
#
# for i in range(1 , n+1):
#     total += i
#
# while True:
#     total +=n
#     n -= 1
#     if n == 0:
#         break
#
# print(total)


# 입력 받은 숫자의 합 구하기 (리스트)
# score = [1,2,3,4,5,6,7,8,9,10]
# score = list(map(int, input("정수 입력: ").split()))
# total = 0
#
# for i in range(0,len(score)):
#     total += score[i] # total +=1
#
# for e in score:
#     total += e
#
# print(total)

# 제곱
# sqare = list(map(lambda a: a**2, [1,2,3,4,5,6,7,8,9,10]))
# print(sqare)
#
# # 입력값 역순
# for i in range(len(score) -1 , -1, -1):
#     print(score[i], end=" ")

#별 100
# for i in range(10): # 초기값은 디폴트 0임/ 최대/증감값 +1 (기본값)
#     print(f"i={i}", end=" ")
#     for j in range(10):
#         print("*", end=" ")
#     print()


"""

for i in range(1,6): # 초기값은 디폴트 0임/ 최대/증감값 +1 (기본값)
    print(f"\ni={i}", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(6,1,-1): # 초기값은 디폴트 0임/ 최대/증감값 +1 (기본값)
    print(f"\ni={i}", end=" ")
    for j in range(i-1):
        print("*", end=" ")
    print()

# break    : 반복문 자체를 즉시 종료
# continue : 현재 반복의 남은 코드를 건너뛰고 다음 반복으로 넘어감

n = int(input("정수 입력: "))
for invert in range(n):
    if invert % 2 == 0: continue
    print(f"값:{invert}")

m = int(input("정수 입력: "))
for butter in range(m):
    if butter % 3 == 0:
        continue
    if butter % 5 == 0:
        continue
    print(f"값:{butter}")

"""

# 휴대폰 요금 계산
"""
## 문제

동호는 새악대로 T 통신사의 새 핸드폰 옴머나를 샀다. 
새악대로 T 통신사는 동호에게 다음 두 가지 요금제 중 하나를 선택하라고 했다.

1. 영식 요금제
2. 민식 요금제

영식 요금제는 30초마다 10원씩 청구된다. 
이 말은 만약 29초 또는 그 보다 적은 시간 통화를 했으면 10원이 청구된다. 
만약 30초부터 59초 사이로 통화를 했으면 20원이 청구된다.

민식 요금제는 60초마다 15원씩 청구된다. 
이 말은 만약 59초 또는 그 보다 적은 시간 통화를 했으면 15원이 청구된다. 
만약 60초부터 119초 사이로 통화를 했으면 30원이 청구된다.

동호가 저번 달에 새악대로 T 통신사를 이용할 때 
통화 시간 목록이 주어지면 어느 요금제를 사용 하는 것이 저렴한지 
출력하는 프로그램을 작성하시오.

## 입력

동호가 저번 달에 이용한 통화의 개수 N이 주어진다. 
N은 20보다 작거나 같은 자연수이다. 
둘째 줄에 통화 시간 N개가 주어진다. 
통화 시간은 10,000보다 작거나 같은 자연수이다.

## 출력

첫째 줄에 싼 요금제의 이름을 출력한다. 
그 후에 공백을 사이에 두고 요금이 몇 원 나오는지 출력한다. 
만약 두 요금제의 요금이 모두 같으면 영식을 먼저 쓰고 민식을 그 다음에 쓴다.

영식은 Y로, 민식은 M으로 출력한다.
"""