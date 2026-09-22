# # 리스트 : 연속적으로 저자되는 형태의 자료형
# # 크기 지정이 필요 없음 / 같은 데이터형일 필요가 없음 / 읽고 쓰기가 가능
# # [] 대괄호로 감싸서 표현, 0개의 이상의 원소가 저장
# # from 내장함수 import score_list
#
# mixed = ["안유진",23,True,[100,200,300]],["서울","대전","대구","부산"],{"주소": "경기도"}
# print(mixed)
#
# # score = list(map(int, input("성적입력: ").split()))
# # print(f"총점:{sum(score)}, 평균:{sum(score) / len(score)}")
#
# # 안유진 출력
# print(mixed[0][0])
#
# #100,200,300 출력
# print(mixed[0][3])
#
# # 안유진
# print(mixed[0][0:3])
#
# print(mixed[1][1])
# print(mixed[1][1][1])
#
# print(mixed[2]["주소"][0])
#
# print(mixed[1][3][0])
#
# # 요소 추가
# list_a =[1,2,3]
# list_a.append(4)
# list_a.append(5)
# list_a.insert(1,1000) # 1번 인덱스에 1000의 값을 넣음
# print(list_a)
# list_a.append([500,600])
# print(list_a)
#
# # 리스트 제거
# # pop: 인덱스가 없으면 맨 마지막값 제거,
# # print(list_a.pop(1)) #1000 삭제
# # print(list_a)
#
# print(list_a.remove(1000)) # none은 값이 없어서
# print(list_a)
#
# del list_a[1] # 1번 인덱스 삭제
# print(list_a)
#
# list_a.clear() # 다 날림
# print(list_a) # 리스트안에 값 없음
#
# # 중복 제거
# my_list = ['a','b','c','d','b','d','e']
# print(my_list)
# new_list = []
# for item in my_list:
#     if item not in new_list:
#         new_list.append(item)
# print(new_list)
#
# # 집합으로 중복 없애기
# test_list = {'a','b','c','d','b','d','e'} # 그냥 알아서 중복 제거함 그러나 순서 유지 안해줌
# print(test_list)
#
#
# # 10개의 임의의 숫자를 입력받아 홀수와 짝수
# score_number = list(map(int, input("숫자 입력: ").split()))
# score_list=[]
# score2_list=[]
#
# odd = list(filter(lambda x: x % 2 == 1, score_number))
# even = list(filter(lambda x: x % 2 == 0, score_number))
# print(f"홀수:{odd}")
# print(f"짝수:{even}")
#
# for number in score_number:
#     if number % 2==0:
#         score_list.append(number)
#     else:
#         score2_list.append(number)
# # print(score_number)
# print(score_list)
# print(score2_list)
#
#

# 3개의 햄버거와 2개의 음료의 가격을 입력 받아 제일 싼 세트 메뉴의 가격 구하기
# 콘솔로 연속해서 햄버거 3개 가격과 음료 2개의 가격을 입력 받음
# 햄버거 3개 중 가장 싼 가격을 선택하고 음료들 중 싼 음료의 가격을 합산 (둘이 합쳐서) 여기서 -50
# 한개의 리스트 구현
prices = list(map(int, input("가격 입력하기: ").split()))


hamburger_prices = prices[:3]
drink_prices = prices[3:]


# cheap_hamburger = min(hamburger[0])
# cheap_juice = min(hamburger[1])

total = min(hamburger_prices) + min(drink_prices) - 50

print(f"총 결제 금액: {total}원입니다.")

