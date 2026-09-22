# 자료형 : 데이터를 저장하는 방시과 연산할 수 있는 방법을 정의하는 데이터의 형태를 의미
#  Python에서는 변수르 선언할 때 자료형을 명시하지 않아도 되며, 값이 핟당이 되면 자동으로 자료형이 결정
# 여기서 의문점 자동으로 결정이 된다고 했는데 그 기준이 무엇이냐?

# text=None # "",100,3.14,True,None
# print(type(text)) # 보시다 시피 값을 어떤것을 넣냐에 따라 int,float,str,bool이 될수도 있다 .
#
# # 문자열 : 문자가 연속으로 존재하는것, python 문자와 문자열 구분 하지 않음 "",'',""" """ , ''' '''
# text1="안녕하세요. 파이썬 입니다."
# print(text1)
# print(text1[0]) # 해당 인덱스를 추출함 "안"은 인덱스 0번 부터 시작해서 추출한것
# print(text1[7:10]) # 이 방식은 슬라이싱 이게 왜 7이냐고 하면 공백도 인덱스에 포함이 됩니다.
# # 안[0] 녕[1] 하[2] 세[3] 요[4] .[5] 공백[6] 파[7] 이[8] 썬[9]
# # 7:10이라고 적었지만 10은 미만을 의미해서 출력이 되지 않음
#
# print(text1 + "!!!!") # 연결하는 것
# print(text1*3) # 반복하는 것
#
# #숫자형 (Number) : 정수, 실수, 복소수형 존재하며, 사칙연산이 가능함
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
# # 불리언(Boolean) : 참과 거짓 두가자의 값만 가짐
# age= int(input("나이를 입력: "))
# is_adult = False
# if age >= 18:
#     is_adult = True
# else:
#     is_adult = False
#
# print(bool(1)) #True   값이 있냐 없냐의 기준으로 True False로 나뉘어집니다.
# print(bool(-1)) # 값이 있음 정수형은 0을 제외하면 다 트루임
# print(bool(0)) # 0이라 없음
# print(bool("")) # 값이 없음
# print(bool(" ")) # 이건 트루임 왜냐 공백도 문자열로 취급해서 값이 있는걸로 판단해서 True
# print(bool(None)) # none은 그냥 없는거임


# 형변환 : 데이터를 다른 자료형으로 바꾸는 것
print("100"+ "200"+"300"+"400"+"500"+"600" )
print(int("100")+200+300+400+500+600)


age= int(input("\n나이를 입력: "))

if age >= 19:
    print("성인입니다.")
else:
    print("미성년자입니다.")

# sentence= "\nPython programming is fun"
# 첫 6글자 ("Python")만 출력하세요
sentence= "\nPython programming is fun"
print(sentence[0:7])
