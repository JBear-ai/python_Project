# 제어문 : 프로그램의 흐름을 제어하는데 사용
# 조건문 : 입력 값에 따라 특정 코드 블록을 선택적 사용 (if, switch, 3항연산자)
# 반복문 : 조건이 충조되는 동안 특정 코드 반복 (while, for)




# - 3자의 정수를 입력을 받아 100의자리, 10자리, 1의 자리로 나누어 담고 가장 큰수를 찾아서 출력
# - 예) 입력 : 574, 출력 : 7

# 3자리 정수를 입력받아 각 자리의 숫자를 분리하고
# 그중 가장 큰 숫자를 출력
# 예) 입력 : 574 → 출력 : 7

number = int(input("정수를 입력하세요: "))

num1 = number // 100
num2 = (number // 10) % 10
num3 = number % 10


# 1. 중첩 if문을 이용한 풀이
# → 두 숫자를 먼저 비교하여 후보를 좁힌 후,
#   남은 숫자와 다시 비교한다.

if num1 > num2:
    if num1 > num3:
        print(f"중첩 if문의 값:{num1}")
    else:
        print(f"중첩 if문의 값:{num3}")
else:
    if num2 > num3:
        print(f"중첩 if문의 값:{num2}")
    else:
        print(f"중첩 if문의 값:{num3}")


# 2. 논리 연산자를 이용한 풀이
# → 각 숫자가 나머지 두 숫자보다 큰지를
#   and를 사용하여 동시에 확인한다.

if num1 > num2 and num1 > num3: # num1이 num2보다 크고 동시에 num3보다 크다면 num1이 가장 큼
    print(f"논리 연산자 값:{num1}")
elif num2 > num1 and num2 > num3: # num1이 가장 큰 조건이 아니었다면, num2가 num1과 num3보다 큰지 확인
    print(f"논리 연산자 값:{num2}")
else:                              # num1도 아니고 num2도 가장 큰 경우가 아니므로 num3 출력
    print(f"논리 연산자 값:{num3}")  # 앞의 두 조건이 모두 거짓인 나머지 경우를 처리한다


# 3. Python 내장함수 max()
# → 가장 큰 값을 찾는 기능을 이미 제공하므로
#   실제 Python에서는 간단하게 해결할 수 있다.
print(f"정수의 자리중 제일 큰 값은(내장 함수): {max(num1, num2, num3)}")


# --------------------------


#
# if num1 > num2:
#     print("num1")
# elif num2 > num3:
#     print("num2")
# else:
#     print("num3")


# "사용자가 상품을 구매할 경우 구매 금액이 5만 원 이상이면 무료배송을 적용하고,
# 회원 등급이 VIP인 경우 구매 금액과 관계없이 무료배송을 적용한다."
"""
price = int(input("구매금액 입력: "))
grade = input("회원님의 등급: ")
addr = "제주"
abc = "특정상품"
if price > 50000:
    print("무료배송 대상자 입니다.")
elif grade == "VIP":
    print("무료배송 대상자 입니다.")
else:
    print("유료 배송 대상자 입니다.")

if (price >= 50000 or grade == "VIP") and  (addr !="제주" and abc!="특정상품" ):
    # 비용이 50,000이 넘거나 또는 비용은 넘지 않았는데 등급이 VIP면 무료 배송자임
    # 특이사항으로 거리가 먼 제주도나 특정상품들 대상으로는 추가 비용이 발생함
    # 괄호로 묻어 저 2가의 조건이 둘다 참이면 무료배송으로 취급 하나라도 틀리면 유료 배송 및 추가 비용 발생
    print("무료 배송 대상자")
else:
    print(f"회원님의 구매 금액은{price}원이며, 배달비가 청구될수 있습니다.")
    print("그 외엔 추가 비용이 발생 할수 있습니다.")
"""

""" """"""""""""""""""""
              핵심
[문제] 
3개의 숫자 중 가장 큰 숫자를 찾아라
        ↓
[조건문으로 해결]
각 숫자가 다른 숫자보다 큰지 비교
        ↓
[중첩 if]
단계적으로 비교해서 후보를 좁힌다
        ↓
[논리 연산자]
A가 B보다 크고 AND A가 C보다 큰가?
        ↓
[Python]
max()라는 내장함수를 이용하면 더 간단하게 가능
""" """"""""""""""""""""


"""
* 홈쇼핑 결제 프로세스 

배송
1.기본 배송비
구매금액 50,000원 이상 → 무료
또는 VIP → 무료
그 외 → 3,000원

2.제주 추가비용  Like %제주%
제주 → +3,000원

3.특정상품 추가비용
특정상품 → +2,000원  리스트를 이용해볼까요?

4.할인
회원등급별 할인
VIP
100,000원 이상 → 30%
50,000원 이상 → 20%
그 미만 → 10%

GOLD
100,000원 이상 → 20%
50,000원 이상 → 15%
그 미만 → 5%

SILVER
100,000원 이상 → 10%
50,000원 이상 → 5%
그 미만 → 3%

일반 → 0%

5.쿠폰
쿠폰이 있으면 추가 5% 할인
없으면 0%
"""
price = int(input("구매금액 입력: ")) # 50000원 넘으면 무료 배송
grade = input("회원님의 등급 (VIP,GOLD,SILVER)\n: ").upper() # 등급에 따라 할인율 및 무료배송 구분
addr = input("지역을 기입해주세요: ") #제주도인지 확인 여부
prod_name = input("상품명: ") # 상품 이름 적기

special_prod = ['TV','김치냉장고','냉장고','에어컨'] # 특정 상품리스트에 해당하면 +=3000
has_coupon = input("쿠폰 사용 여부 (Y/N):  ").upper()

# 1. 기본 배송비
if price >= 50000 and grade == "VIP":
    delivery_fee=0
else:
    delivery_fee = 3000

# 2. 거리가 먼 경우 추가비용 발생
if "제주" in addr:
    delivery_fee += 3000

# 3. 특정 상품인가?
# if prod_name == special_prod: 이렇게 작성시 둘이 똑같은가로 인식함 (피드백1)
if prod_name in special_prod: # in을 작성시 리스트안에 들어가 있는가로 인식
    delivery_fee += 3000

#4. 등급별 할인
if grade == "VIP":
    if price >= 100000:
        discount_rate=0.30
    elif price >= 50000:
        discount_rate=0.20
    else:
        discount_rate=0.10
elif grade == "GOLD":
    if price >= 100000:
        discount_rate=0.20
    elif price >= 50000:
        discount_rate=0.15
    else:
        discount_rate=0.05  # 오타 확인
elif grade == "SILVER":
    if price >= 100000:
        discount_rate=0.10
    elif price >= 50000:
        discount_rate=0.05
    else:
        discount_rate=0.03
else:
    discount_rate=0

# 5. 쿠폰 할인 여부
# if has_coupon: 이렇게 작성시 Y,N을 넣든 둘다 True 인식 (피드백2)
if has_coupon == "Y":
    coupon_rate = 0.05
else:
    coupon_rate = 0

# ----------------------------------
member_discount = price * discount_rate
coupon_discount = price * coupon_rate

final_price = price - member_discount - coupon_discount + delivery_fee

print(f"상품금액: {price}원") # 구매한 제품원가 기호 부여 X
print(f"회원 할인: -{member_discount:.0f}원") # 할인이니 -
print(f"쿠폰 할인: -{coupon_discount:.0f}원")
print(f"배송비: +{delivery_fee}원") # 추가비용 발생 시 +
print(f"최종 결제금액: {final_price:.0f}원")

