import json
books = [
    {
        "title": "클린 코드",
        "author": "로버트 C. 마틴",
        "publisher": "인사이트",
        "year": 2013,
        "price": 33000,
        "genre": ["IT/프로그래밍", "소프트웨어공학"]
    },
    {
        "title": "파이썬 코딩의 기술",
        "author": "브렛 슬라트킨",
        "publisher": "길벗",
        "year": 2020,
        "price": 32000,
        "genre": ["IT/프로그래밍", "파이썬"]
    },
    {
        "title": "달러구트 꿈 백화점",
        "author": "이미예",
        "publisher": "팩토리나인",
        "year": 2020,
        "price": 13800,
        "genre": ["소설", "판타지"]
    },
    {
        "title": "사피엔스",
        "author": "유발 하라리",
        "publisher": "김영사",
        "year": 2015,
        "price": 22000,
        "genre": ["인문", "역사"]
    },
    {
        "title": "코스모스",
        "author": "칼 세이건",
        "publisher": "사이언스북스",
        "year": 2006,
        "price": 19500,
        "genre": ["과학", "천문학"]
    }
]

# 2번
json_book = json.dumps(books, ensure_ascii=False, indent=4)
print(json_book)

# 3번
obj = json.loads(json_book)
print("-----------------------------------")
print(obj)
print("-----------------------------------")


print("**************************************")
for e in obj:
    print(e)
print("**************************************")
# 4번
for e in obj:
    if e["price"] >=30000:
        print(f"{e["title"]} - {[e["price"]]}") # 계산식으로 인식해서 {} 두개로 나누어서 사용해야함

# 5번
with open('Book.json', 'w', encoding='utf-8') as json_file: # 쓰기
    json.dump(books, json_file, ensure_ascii=False, indent=4)

with open('Book.json', 'r', encoding='utf-8') as json_file: # 읽기
    Book = json.load(json_file)


# 6번
author =input("작가의 이름을 입력하세요: ")

for e in Book:
   if e["author"] == author:
    print(e["title"])