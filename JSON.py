# JSON(JavaScript Object Notation) 데이터를 저장하고 교환하는 데 널리 사용되는 경량 텍스트 형식
# -파이썬에서는 JSON 기본 라이브러리를 통해 사용 가능
# -경량 텍스트 포맷
# -키와 값으루 구성
# -언어 독립적
# -웹 API 통신, 설정 파일, 데이터 저장 및 교환 등 다양한 분야에서 활용

import json
# 파이썬 객체를 JSON으로 직렬화
# 회원 정보 (이름, 주소, 나이, 성별, 포지션, 전화번호 2개 )

members = [
    {
        "name": "안유진",
        "addr": "대전시",
        "age": 23,
        "gender": "여성",
        "phone": ["010-1234-7867", "041-123-7988"],
        "position": "리더"  # 리더,서브리더,멤버
    },
    {
        "name": "가을",
        "addr": "인천시",
        "age": 24,
        "gender": "여성",
        "phone": ["010-2345-6789", "032-234-5678"],
        "position": "멤버"
    },
    {
        "name": "레이",
        "addr": "서울시",
        "age": 22,
        "gender": "여성",
        "phone": ["010-3456-7890", "02-345-6789"],
        "position": "멤버"
    },
    {
        "name": "장원영",
        "addr": "서울시",
        "age": 22,
        "gender": "여성",
        "phone": ["010-4567-8901", "02-456-7890"],
        "position": "멤버"
    },
    {
        "name": "리즈",
        "addr": "제주시",
        "age": 22,
        "gender": "여성",
        "phone": ["010-5678-9012", "064-567-8901"],
        "position": "멤버"
    }
]


# Python 객체를 JSON으로 직렬화
json_str = json.dumps(members, ensure_ascii=False, indent=4) # 아스키가 아니고 들여쓰기 4칸
print(json_str)

# JSON을 → Python으로 역직렬화
obj = json.loads(json_str)
print(obj)

print("--------------------------------------")
for e in obj:
    print(e)
print("--------------------------------------")

# 파일로 저장 하기(쓰기) W
# wtih는 파일을 자동으로 닫아 줌
with open('date.json', 'w', encoding='utf-8') as json_file:
    json.dump(members, json_file, ensure_ascii=False, indent=4)

# 파일에서 읽기 r
with open('date.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
print(data)

