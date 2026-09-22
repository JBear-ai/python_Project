import pymysql

def connection():
    # DB 연결 함수 만듬
    conn = pymysql.connect(host="127.0.0.1", user="root", port=3306,
                           password="1234", database="mysqlDB", charset="utf8mb4")
    cur = conn.cursor()
    return conn,cur

    # 밖에다가 DB를 연결함 매번 연결하기 싫어서


def login_input():
    # 1번 선택시 로그인 화면 출력후 입력 값 받고 검증까지 통과시 게시판 메뉴로 실패 시 로그인상태 화면으로 돌아가기
    conn,cur=connection()
    user_id = input("ID 입력: ")
    user_pwd = input("PWD 입력: ")
    cur.execute("SELECT * FROM userTable WHERE id=%s AND pwd=%s", (user_id,user_pwd ))
    rows = cur.fetchone()
    if rows:
        print("로그인 성공")
        print(f"{rows[2]}님 환영합니다")
        conn.close()
        return user_id # 스텝 2번의 반환값 ID만
    else:
        print("ID 및 PWD가 일치하지 않습니다.")
        print("다시 시도하거나 회원가입을 해주세요.")
        conn.close()
        return None
## -------------------------------------------------


def create_user_table():
    #DB 테이블 생성 뼈대 생성
    conn,cur=connection()
    # cur.execute("DROP TABLE IF EXISTS userTable")
    cur.execute("""
        CREATE TABLE IF NOT EXISTS userTable (
            id CHAR(20) PRIMARY KEY,
            pwd CHAR(20) NOT NULL,
            name CHAR(20) NOT NULL,
            email CHAR(20) NOT NULL,
            addr CHAR(50)
        )
    """)

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

# ---------------------------------------
def print_login():
    # 로그인 상태 확인하기 위한 기능 구현
    while True:
        print("\n===== 로그인 상태 =====")
        print("1. 로그인")
        print("2. 회원가입")
        print("3. 종료 ")

        choice_login = input("선택: ")
        if choice_login == "1":
           current_user =login_input()
           if current_user:
               print_menu(current_user) # 스텝2번의 id반환

        elif choice_login == "2":new_user_insert()
        elif choice_login == "3":
            print("프로그램 종료 !!!!")
            break
        else:
            print("잘못된 입력 입니다. 다시 선택 하세요.")

#  ---------------------------


## ----------------
def create_boardTable():
    #과제 테이블 생성 1
    conn,cur=connection()
    # cur.execute("DROP TABLE IF EXISTS boardTable")
    cur.execute("""
        CREATE TABLE IF NOT EXISTS boardTable (
            b_id BIGINT auto_increment PRIMARY KEY, -- 글번호
            b_title VARCHAR(20) NOT NULL , -- 제목
            b_text VARCHAR(1000) NOT NULL , -- 내용
            writer CHAR(20) NOT NULL , -- 작성자
            reg_date DATETIME DEFAULT current_timestamp, -- 작성일 
            
            FOREIGN KEY (writer) REFERENCES userTable (id)                                                
        )
    """)
    # 2개가 자동등록이라 3개의 컬럼을 등록
    boards = [
        ('파이썬 질문입니다', '반복문을 공부하다가 궁금한 점이 생겼습니다.', 'ayj1234'),
        ('MySQL 공부 중입니다', '외래키와 기본키의 차이를 공부하고 있습니다.', 'jwy1234'),
        ('오늘 수업 정리', '오늘은 데이터베이스 CRUD에 대해 학습했습니다.', 'fall1234'),
        ('게시판 테스트', '게시판 글 작성 기능을 테스트하고 있습니다.', 'ys1234'),
        ('PyMySQL 질문', '파이썬에서 MySQL 연결 방법을 연습하고 있습니다.', 'lay1234')
    ]

    for board in boards:
        cur.execute("INSERT INTO boardTable(b_title, b_text, current_user) VALUES(%s, %s, %s)", board)

    # 커밋 및 연결 종료
    conn.commit()
    conn.close()


def create_commentTable():

    conn, cur = connection()
    # cur.execute("DROP TABLE IF EXISTS commentTable")
    cur.execute("""
                CREATE TABLE IF NOT EXISTS commentTable
                (
                    C_num     BIGINT auto_increment PRIMARY KEY, -- 댓글 번호
                    C_number  BIGINT(20) NOT NULL ,             -- 게시글 번호  boardTable 참조하는 외래
                    C_writer CHAR(20) NOT NULL,               -- 작성자    userTable 참조하는 외래
                    C_text   VARCHAR(1000) NOT NULL ,           -- 내용                    
                    C_reg_date DATETIME DEFAULT current_timestamp, -- 작성일 
                    
                    FOREIGN KEY (C_number) REFERENCES boardTable(b_id) -- 게시글 삭제시 댓글도 삭제
                        ON DELETE CASCADE,                                                
                        
                    FOREIGN KEY (C_writer) REFERENCES userTable(id) -- 작성자 참조                                        
                )
                """)

    comments = [
        (1, 'jwy1234', '저도 반복문 처음 배울 때 헷갈렸어요.'),
        (1, 'fall1234', 'for문과 while문을 비교해보면 이해하기 좋습니다.'),
        (2, 'ayj1234', '외래키는 다른 테이블과의 관계를 연결해주는 역할입니다.'),
        (3, 'ys1234', 'CRUD 정리 내용 잘 봤습니다.'),
        (5, 'lay1234', 'PyMySQL 연결 부분 저도 연습 중입니다.')
    ]

    for comment in comments:
        cur.execute(
            "INSERT INTO commentTable(C_number, C_current_user, C_text) VALUES(%s, %s, %s)",
            comment
        )

    conn.commit()
    conn.close()




# 1번 회원가입 : insert()
def new_user_insert():
    conn,cur=connection()
    print("\n===== 회원가입 창=====")
    # id = input("아아디 : ")
    # if id == 'exit' : return "exit"
    # cur.execute("SELECT * FROM userTable WHERE id=%s", (id,))
    # rows = cur.fetchone()
    while True:
        id = input("아아디 : ")
        if id == 'exit': return "exit"
        cur.execute("SELECT * FROM userTable WHERE id=%s", (id,)) # DB 에게 검색을 시킴
        rows = cur.fetchone() # 검색 결과를 파이썬에서 가져올것
        if rows: # 가져온 결과를 판단
            print("중복된 아이디 입니다.")
            continue # 중복이 맞다고 판단시 다시 아이디로 돌아감
        else:
            break # 중복이 아니면 pwd로 이어짐
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

# 3번 게시글 작성
def insert_board():
    conn, cur = connection()



## 5번 댓글 작성
def new_comment_insert():
    conn,cur=connection()
    C_number = input("")
    C_current_user = input("")
    C_text = input("")
    try:
        cur.execute("INSERT INTO commentTable VALUES(%s, %s, %s)", (C_number, C_current_user, C_text))
        print("댓글 작성 완료!!")
    except Exception as e:
        print(f"오류 발생: {e}")

    # 존재하는 게시글 번호인지?
    # 로그인된 사용자 id를 작성자로 하여 commentTable에 저장

    conn.commit()
    conn.close()
## ------

## 6번 게시글 삭제
def delete_board():
    conn, cur = connection()
    id = input("삭제할 게시글 ID : ")
    cur.execute("DELETE FROM usertable WHERE id = %s", id)
    if cur.rowcount > 0:
        print("삭제 성공 !!")
    else:
        print("해당 글에 대한 권한이 없습니다.")
    conn.commit()
    conn.close()


def print_menu(current_user):
    while True:
        print("\n===== 게시판 메뉴 =====")
        print(f"현재 로그인 사용자: {current_user}")

        print("1. 게시글 작성")
        print("2. 게시글 수정")
        print("3. 게시글 삭제")
        print("4. 게시글 조회")
        print("5. 댓글 작성")
        print("6. 로그아웃")

        choice = input("메뉴 선택 : ")

        if choice == "1":
            # new_board_insert(current_user)
            pass
        elif choice == "2":
            # 게시글 수정 함수
            pass

        elif choice == "3":
            # 게시글 삭제 함수
            pass

        elif choice == "4":
            # 게시글 조회 함수
            pass

        elif choice == "5":
            new_comment_insert(current_user)

        elif choice == "6":
            print("로그아웃 합니다.")
            break

        else:
            print("잘못된 입력 입니다. 다시 선택하세요.")

if __name__ == "__main__":
    create_user_table()
    create_boardTable()
    create_commentTable()
    # print_login()
