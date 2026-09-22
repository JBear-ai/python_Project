# n = int(input("통화건수을 입력하세요: "))
# call = list(map(int,input("통화 시간을 입력하세요: ").split()))
#
# # n은 건수이다 20보다 작거나 자연수
# # 영식이는 Y  민식이는 M
#
# y_call = 0
# m_call = 0
# for i in range(n):
#     # if call[i] <= 20:
#         y_call += (call[i] // 30) * 10 +10
#         m_call += (call[i] // 60) * 15 + 15
#
# if y_call > m_call:
#     print("M", m_call)
# elif y_call < m_call:
#     print("Y", y_call)
# else:
#     print("Y,M", y_call)


even_cnt = 0
odd_cnt = 0
while True:
    number = int(input("정수입력: "))
    if number == -1:
        break
    if number % 2 == 0:
        even_cnt += 1
    else:
        odd_cnt += 1
print(f"갯수: {even_cnt}")
print(f"갯쉬 {odd_cnt}")

while True:
    den = int(input("2~9 사이의 정수 입력: "))
    if 2<= den <=9:
        break
    print("잘못된 입력 입니다.")

for i in range(1, 10):
    print(f"{den} x {i} = {den * i}")















n = int(input("통화 건수를 입력하세요: "))
call = list(map(int, input("통화시간을 입력하세요: ").split()))

y_call = 0
m_call = 0

for i in range(n):
    y_call += (call[i] // 30) * 10 + 10
    m_call += (call[i] // 60) * 15 + 15

if y_call > m_call:
    print("M", m_call)
elif y_call < m_call:
    print("Y", y_call)
else:
    print("Y M", y_call)

ABC = list(map(int, input("통화시간을 입력하세요: ").split()))

