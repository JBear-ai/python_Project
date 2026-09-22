import pymysql

def connection(): # 연결 함수
    conn = pymysql.connect(host="127.0.0.1", user="root", port=3306,
                           password="1234", database="mysqlDB", charset="utf8mb4")
    cur = conn.cursor()
    return conn,cur

# 1. DB 연결
# def get_connection():
#     conn = pymysql.connect(host="127.0.0.1", user="root", port=3306,
#                        password="1234", database="mysqlDB", charset="utf8mb4")
#     return conn

def create_user_table(): #DB 테이블 생성
    conn,cur=connection()
    cur.execute("DROP TABLE IF EXISTS userTable")
    cur.execute("""
        CREATE TABLE userTable (
            id CHAR(10) PRIMARY KEY,
            pwd CHAR(15),
            name CHAR(20),
            email CHAR(20),
            addr CHAR(50)
        )
    """)

#  초기 데이터 삽입
# def insert_user(conn):
#     cur = conn.cursor()
    users = [
        ('ayj1234', '12345678', '안유진', 'ayj@gmail.com', '서울시 강남구'),
        ('jwy1234', '12345678', '장원영', 'jwy@gmail.com', '서울시 강남구'),
        ('fall1234', '12345678', '가을', 'fall@gmail.com', '서울시 강남구'),
        ('ys1234', '12345678', '이서', 'ws@gmail.com', '서울시 강남구'),
        ('lay1234', '12345678', '레이', 'lay@gmail.com', '서울시 강남구')
    ]

    for user in users:
        cur.execute("INSERT INTO userTable VALUES(%s, %s, %s, %s, %s)", user)

    # 커밋 및 연결 종료
    conn.commit()
    conn.close()

# 사용자 추가 : insert()
def new_user_insert():
    conn,cur=connection()

    id = input("아아디 : ")
    if id == 'exit' : return "exit"
    pwd = input("패스워드 : ")
    name = input("이름 : ")
    mail = input("이메일 : ")
    addr = input("주소 : ")
    try:
        cur.execute("INSERT INTO userTable VALUES(%s, %s, %s, %s, %s)", (id, pwd, name, mail, addr))
        print("사용자 추가 완료!!")
    except Exception as e:
        print(f"오류 발생: {e}")

    conn.commit()
    conn.close()




# def main():
#     # conn = get_connection()
#     create_user_table(conn)
#     # conn = get_connection()
#     # insert_user(conn)
#
#     while True:
#         # conn = get_connection()
#         rst = new_user_insert(conn)
#         if rst == "exit": break
#
#
# if __name__ == "__main__":
#     main()

# 조회 기능
def select_sql(): #회원 조회
    conn,cur=connection()
    cur.execute("SELECT * FROM userTable")
    rows = cur.fetchall()
    print("ID       비밀번호        이름      이메일     주소")
    print("----------------------------------------------")
    for row in rows:
        print(f"{row[0]:10}   {row[1]:12}   {row[2]:10}   {row[3]:15} {row[4]:45}")
    conn.close()

def update_user(): # 회원 수정
    conn, cur = connection()
    id = input("ID(필수 사항): ")
    name = input("변경할 이름: ")
    email = input("변경할 이메일: ")
    addr = input("변경할 주소: ")
    cur.execute("UPDATE usertable SET name=%s, email=%s, addr=%s WHERE id=%s", # 조건 아이디 검색
                (name, email, addr, id))
    if cur.rowcount > 0:
        print("수정 완료!!")
    else:
        print("해당 ID는 존재 하지 않습니다.")
    conn.commit()
    conn.close()

def delete_user(): # 회원 삭제
    conn, cur = connection()
    id = input("삭제할 사용자 ID : ")
    cur.execute("DELETE FROM usertable WHERE id = %s", id)
    if cur.rowcount > 0:
        print("삭제 성공 !!")
    else:
        print("해당 ID가 존재하지 않습니다.")
    conn.commit()
    conn.close()





def print_menu():
    while True:
        print("\n===== 사용자 관리 메뉴 =====")
        print("0. 테이블 생성")
        print("1. 사용자 추가")
        print("2. 사용자 수정")
        print("3. 사용자 삭제 ")
        print("4. 사용자 조회")
        print("5. 종료")

        choice = input("메뉴 선택 : ")
        if choice == "0": create_user_table()
        elif choice == "1": new_user_insert()
        elif choice == "2": update_user()
        elif choice == "3": delete_user()
        elif choice == "4": select_sql()
        elif choice == "5":
            print("프로그램 종료 !!!!")
            break
        else:
            print("잘못된 입력 입니다. 다시 선택 하세요.")

if __name__ == "__main__":
    print_menu()
