# 문자열 : 파이썬은 문자와 문자열 구분안함 str ',"

# 문자열 인덱싱 슬라이싱
# text = "안녕하세요. 파이썬 입니다"
# print(text[0])
# print(text[1])
# print(text[7])
# print(text[13])# or -1
#
# print(text[7:11])
# print(text[::2]) # :: 안 2번 뛰고 '하' 2번뛰고 '요'
# print(text[:2]) # 0~2까지
# print(text[::-1]) # 처음에서 마지막까지 역순


# 주민등록번호 : 980410 - 1575123
# 성별 : 남성
# 나이 : 25세

# from datetime import datetime
# current_year = datetime.now().year
#
# jumin = input("주민등록번호 입력(하이픈 포함) : ") # 971018-1
# year = int(jumin[:2]) # 년도
# month = int(jumin[2:4]) #월
# day = int(jumin[4:6]) # 일
# gender = int(jumin[7]) # 하이픈 포함으로 뒷자리 첫번째
# # age = jumin[:2] # 년도
#
#
# if gender == 1 or gender == 2: # 생년월일
#     birthday = f"{year + 1900}년{month}월{day}일"
# else:
#     birthday = f"{year + 2000}년{month}월{day}일"
#
#
# gen = "" # 성별 빈값 대입
# if gender == 1 or gender == 3: # 뒷자리가 1또는 3이여야 남성 그외는 여성
#     gen="남성"
# else:
#     gen="여성"
#
#
# print(f"생년월일 : {birthday}")
# print(f"성별 : {gen}")
#
# if gender == 1 or gender == 2:
#     print(f"나이 : {current_year - (year + 1900) }")
# else:
#     print(f"나이 : {current_year - (year + 2000)}")


# 대소무자 바꾸기 : upper() 와 lower
# a= "Hello World"
# print(a.upper())
# print(a.lower())
#
# #isupper(), islower()
# # 입력 받은 문자열에서 소문자는 대문자로 대문자는 소문자로 변경
# for e in a:
#     if e.islower():
#         print(f"{e.upper()}", end="")
#     elif e.isupper():
#         print(f"{e.lower()}", end="")
#     else:
#         print(e, end="")
#
# print()
#
# #문자열 변경 : replace ("", "")
# input_str ="Hello Python Program"
# new_str = input_str.replace("Python","JavaScript")
# print(new_str)
#
# # 문자 갯수 세기 : .count(char)
# text = "Google kakao naver openAI oole"
# print(text.count("a"))  #
# print(text.count("o"))
# print(text.count("oo")) # char 부분 문자열 추출 2개
#
# # 문자열 길이: len()
# text = "Hello world"
# print(len(text)) # 길이 변환 11

# 문자열 찾기 : find(),rfind(),index()
# find(): 찾은 부분 문자열의 첫 번째 인덱스를 반환합니다. 부분 문자열을 찾지 못하면 -1을 반환합니다.
# index(): 찾은 부분 문자열의 첫 번째 인덱스를 반환합니다. 부분 문자열을 찾지 못하면 ValueError 예외를 발생시킵니다.

phrase = "가장 큰 실수는 포기, 가장 어리석은 일은 남의 결점 찾기, 가장 좋은 선물은 용서"
print(phrase.find("가장")) # 앞에서 시작
print(phrase.rfind("가장")) # 뒤에서 부터 찾지만 인덱스는 앞에서 부터

print(phrase.index("포기"))

print(phrase.find("나에게"))  # 찾는 결과 없으면 -1
# print(input_b.index("나에게")) # 해당 단어가 없으므로 에러가 발생 합니다

new_phrase = phrase.replace("가장", "나에게") # 변경 대상 , 변경 내용
print(new_phrase)

# 공백제거
# .strip(): 양쪽 공백 제거
# .lstrip(): 왼쪽 공백 제거
#. rstrip(): 오른쪽 공백 제거

input_a = """
    안녕하세요.
문자열 함수를 알아 봅니다.

    """
print(input_a.strip())


