# 반복문 : 주어진 조건이 참인 동안 반복 수행 함
# while문 : 주로 반복횟수를 알 수 없을 때
# for문 : 반복 횟수가 정해져 있을때 사용함

"""
n= int(input("정수 입력: "))
total = 0 # 합계를 저정할 변수
while n>0: # 반복문의 조건인 n의 값이 0보다 크면 참으므로 반복 수행
    total += n # total = total + n
    n -=1 # n = n-1 , n의 값을 변경해서 반복문을 빠져 나가게 함

for i in range(1, n+1):
    total += i

print(f"합: {total}")


# while 문은 반복 횟수를 알 수 없을 때 사용하며 좋음
# 성별을 받는데 남성은 M, 여성은 F로 입력 받음, 잘 못된 입력이면 계속 다시 입력 받음

while True: # 무한 반복문 이므로 탈출 조건이 필요합니다.
    gender = input("성별을 입력 하세요: ").upper()
    if gender=="M" or gender=="F":
        break # 유효한 값이 들어가며 종료함
    print("성별을 잘 못 입력 하셨습니다.")

print(f"{'남성' if gender == 'M' else '여성'} 입니다.")

"""

# for 문 : 정해진 범위(range)만큼 반복 수행 할 때 효과적
# for 요소 in 시퀀스:
# for 요소 in range(시작값, 최종값, 증감값):

ive = ["안유진", "장원영", "이서", "가을", "레이", "리즈"]
for e in ive:  # 향상된 for문
    # e += "*"
    print(e, end=" ")

for i in range(0,len(ive),2): # 원래 값은 range(0, len(ive), 1) 범위형
    ive[i] += '/'
    print (ive[i], end=" ")

for i in range(len(ive)-1,0 - 1,-1): # 원래 값은 range(0, len(ive), 1) 범위형
    # ive[i] += '/'
    print(ive[i], end=" ")


for e in ive:
    print(e, end=" ")

# 1~100 사이의 3의 배수 출력
cnt = 0
for i in range(1, 100+1):
    if i % 3 == 0:
        print(f"\n{i:3}", end=" ")
        cnt += 1
        if cnt >=10:
            cnt = 0

# # 입력 받은 수의 범위 내의 7의 배수를 출력
# # 한줄에 10개씩 출력
# # 정렬을 적용해 줄 맞추기 {n:5}
# number = int(input("수를 입력하세요. "))
#
# for i in range(0,len(number)):
#     if i%7 ==0:
#         print(f"\n {number[i]:5}", end=" ")



# 이중 for문
# 입력 받은 수가 10이라면 10*10의 행렬 출력
num11=int(input("정수 입력: "))
cnt = 0
for i in range(1,num11+1):
    for j in range(1,num11+1):
        cnt += 1
        print(f"{cnt:3}", end=" ")
    print()


