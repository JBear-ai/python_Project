# 기본 메뉴 추가
# {} 중괄호를 사용해 선언, 각 요소는 , 쉼표로 구분
# 키와 값은 : 으로 구분
# 딕셔너리 내부에 리스트를 가짐
import json

menu = {
    "americano" : ["coffee", 2000 , "기본 커피 입니다,"],
    "espresso" : ["coffee", 2500 , "진한 커피 입니다,"],
    "latte" : ["coffee", 4000 , "우유가 들어 있는 커피 입니다,"],
    "green tea" : ["tea", 4500 , "녹차 입니다,"],
    "black tea" : ["tea", 4500 , "홍차 입니다,"]
}

# 전체 메뉴 조회
def print_menu():
    for e in menu:
        print(f"{e} - {menu[e]}")

# 개별 메뉴 조회
def get_menu(name):
    if name in menu:
        print(menu[name])
    else:
        print("찾는 메뉴가 없습니다.")

# 메뉴 추가
def add_menu(name, category, price, desc):
    if name not in menu:
        menu[name] = [category, price, desc]
        print(f"{name} 메뉴가 추가 되었습니다.")
    else:
        print("메뉴가 이미 존재 합니다,")

# 메뉴 삭제



# 메뉴 수정


# 파일에서 불러오기
def load_menu():
    try: #예외가 발생하기 쉬운 구간에 사용
        with open("menu.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("해당 파일이 존재 하지 않음")
    except json.decoder.JSONDecodeError:
        print("JSON 디코딩 실패")

# 파일에 저장 하기
def save_menu():
    with open("menu.json", "w", encoding="utf-8") as file:
        json.dump(menu, file, ensure_ascii=False, indent=4)
        print("menu.json 파일에 저장되었습니다.")

# 전체 메뉴 만들기
# [1]전체 메뉴 보기 [2]개별 메뉴 조회 [3]메뉴 추가 [4]메뉴 삭제 [5]메뉴 수정 [6]종료
while True:
    print("메뉴를 선택 하세요: ")
    choice = int(input("[1]전체 메뉴 [2]조회 [3]추가 [4]삭제 [5]수정 [6]종료:  "))

    # if choice == 1:
    #     print_menu()
    # elif choice == 2:


