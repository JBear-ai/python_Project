# with open('스타벅스일일매출.txt', 'r', encoding="utf-8")as file:
#     for e in file:
#         print(e, end='')
#     print()

# 스타벅스 판매량 구하기
file_name = "스타벅스일일매출.txt"
espresso =[] # 빈 리시트 생성
americano = []
cafeLatte = []
cappuccino= []
dates_time = []

with open(file_name, "r", encoding="utf-8") as file:
    header = file.readline().split() # 줄 바꿈 기준으로 한줄 읽어 들임
    # header_line = header.split() # 공백 기준으로 잘라 문자열 리스트 생성
                                 # 9.11 / 10 / 50 / 45 / 20  /(공백 부분 표현)
    for e in file:
        date_list = e.split()
        dates_time.append(date_list[0])
        espresso.append(int(date_list[1])) # 날짜 인덱스가 0이라
        americano.append(int(date_list[2]))
        cafeLatte.append(int(date_list[3]))
        cappuccino.append(int(date_list[4]))
    file.close()

# 제목 / 전체 판매량 /
# print(f"항목: {header[1]} / 전체 판매량: {sum(espresso)}잔 / 일 평균 판매량: {sum(espresso) / len(espresso)}")
# print(f"항목: {header[2]} / 전체 판매량: {sum(americano)}잔 / 일 평균 판매량: {sum(americano) / len(americano)}")
# print(f"항목: {header[3]} / 전체 판매량: {sum(cafeLatte)}잔 / 일 평균 판매량: {sum(cafeLatte) / len(cafeLatte)}")
# print(f"항목: {header[4]} / 전체 판매량: {sum(cappuccino)}잔 / 일 평균 판매량: {sum(cappuccino) / len(cappuccino)}")
# print()
#
# print("항목\t\t\t 전체 판매량\t\t일 평균 판매량")
# print("-"*50)
# print(f"{dates_time[0]}")
# print(f"{header[1]:8}  {sum(espresso):9}잔  {sum(espresso) / len(espresso):14.1f}잔")
# print(f"{header[2]:8}  {sum(americano):9}잔  {sum(americano) / len(americano):14.1f}잔")
# print(f"{header[3]:8}  {sum(cafeLatte):9}잔  {sum(cafeLatte) / len(cafeLatte):14.1f}잔")
# print(f"{header[4]:8}  {sum(cappuccino):9}잔  {sum(cappuccino) / len(cappuccino):14.1f}잔")
#
# print(f"{cafeLatte[2]}\n")


# 실습 문제
"""
1. 각 메뉴별 전체 판매량          메뉴별 sum
2. 각 메뉴별 일 평균 판매량       메뉴별 /
3. 판매량이 가장 높은 메뉴 구하기  max
4. 판매량이 가장 적은 메뉴 구하기  min
5. 판매량이 가장 많은 날짜 구하기  count,len
6. 메뉴 리스트로 만들기  return list? 함수의 반환값은 튜플,리스트[],문자열로 반환받음
"""
# 1번
def total_sales_func():
    print("\n각 메뉴별 전체 판매량")
    print("-"*50)
    print(f"{header[1]}: {sum(espresso)}잔")
    print(f"{header[2]}: {sum(americano)}잔")
    print(f"{header[3]}: {sum(cafeLatte)}잔")
    print(f"{header[4]}: {sum(cappuccino)}잔")


# 2번
def avg_sales_func():
    print("각 메뉴별 일 평균 판매량") # 분모를 날짜 기준으로 잡아야함
    print("-"*50)
    print(f"{header[1]}: {sum(espresso) / len(dates_time):.0f}잔")
    print(f"{header[2]}: {sum(americano) / len(dates_time):.0f}잔")
    print(f"{header[3]}: {sum(cafeLatte) / len(dates_time):.0f}잔")
    print(f"{header[4]}: {sum(cappuccino) / len(dates_time):.0f}잔")


# 3번 판매량이 가장 높은 메뉴 구하기
def most_sold_menu_func():
    pass
# coffee_sum = americano + cafeLatte + cappuccino + espresso
# print(coffee_sum)
# print(f"판매량이 가장 많은 메뉴")
# print(f"{max(header)}:{max(sum(espresso),sum(americano),sum(cafeLatte),sum(cappuccino))}")

espresso_total = sum(espresso)
americano_total = sum(americano)
latte_total = sum(cafeLatte)
cappuccino_total = sum(cappuccino)
print("-"*50)
print(f"판매량이 가장 많은 메뉴")
if espresso_total > americano_total > latte_total > cappuccino_total:
    print(f"에스프레소: {espresso_total}잔")
elif americano_total > latte_total > cappuccino_total:
    print(f"아메리카노: {americano_total}잔")
elif latte_total > cappuccino_total:
    print(f"카페라떼: {latte_total}잔")
else:
    print(f"카푸치노:, {cappuccino_total}잔")


print("-"*50)
# 4번
def best_sold_menu_func():
    pass
print(f"판매량이 가장 적은 메뉴")
if espresso_total < americano_total < latte_total < cappuccino_total:
    print(f"에스프레소: {espresso_total}잔")
elif americano_total < latte_total < cappuccino_total:
    print(f"아메리카노: {americano_total}잔")
elif latte_total < cappuccino_total:
    print(f"카페라떼: {latte_total}잔")
else:
    print(f"카푸치노: {cappuccino_total}잔")


# 5번
def best_sell_menu_func():
    pass
daily_sales=[]
for e in range(len(dates_time)):

    daily_total = espresso[e]+americano[e]+cafeLatte[e]+cappuccino[e]
    daily_sales.append(daily_total)
max_sales = max(daily_sales)
max_total = daily_sales.index(max_sales)  #max_sales이라는 값이 있는지 인덱스에 있는지 찾기
print(f"\n 가장 많이 팔린 날짜는 {dates_time[max_total]}일 ({max_sales}개)")

# print(f"{dates_time[0]}:{str(max(daily_sales))}잔")


# 6번
