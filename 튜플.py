# 튜플
import numbers
from random import random

# ls = [1,2,3]
# tp1 = (1,2,3)
# tp2 = 1,2,3
# ts = 1
# ts2 = "2"
# ts3 =3,
# ts4 = [1,]
# ts5 = {1,2,3} # 딕셔너리가 아닌 이유? 키와 값을 지정
# ts6 = {1,}
#
# print(type(ls))
# print(type(tp1))
# print(type(tp2))
# print(type(ts))
# print(type(ts2))
# print(type(ts3))
# print(type(ts4))
# print(type(ts5))
# print(type(ts6))

member = "안유진", 23, "대전시", True # 패킹
name, age, addr, is_adult = member # 언패킹

# member.append("1004")
# print(member)

def get_name_card(name, phone):
    position = f"{name} 수석 연구원"
    addr = "서울시 강남구"
    phone = f"082+{phone}"
    return position, addr, phone
result  = get_name_card("KMS", "1234-9761")
print(f"{result}")

s1= {1,2,3,4,5,6,7}
s2= {1,5,7,9,10,11,14,15}

s3 = {1,2,3,4,5,6,7,2,3,4,5}
print(s3)

# 교집합
print(s1.intersection(s2))
print(s1 & s2)

# 합집합
print(s1.union(s2))
print(s1 | s2)

# 차집합
print(s1.difference(s2))
print(s1 - s2)

# 복잡한 중복제거
import random
numbers = set()
while True:
    number = random.randint(1, 10)
    if number not in numbers:
        number.append(numbers)
    if len(number) == 5: break
print(number)