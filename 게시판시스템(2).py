import pymysql


# =========================================================
# DB 연결
# =========================================================
def connection():
    # MySQL DB에 연결
    # 다른 함수에서 DB가 필요할때마다 이 함수를 호출해서 conn, cur을 받아옴
    conn = pymysql.connect(
        host="127.0.0.1",
        user="root",
        port=3306,
        password="1234",
        database="mysqlDB",
        charset="utf8mb4"
    )

    # SQL 명령어를 DB에 전달하기 위한 커서 생성
    cur = conn.cursor()

    # 연결 객체와 커서를 호출한 함수에게 반환
    return conn, cur


# =========================================================
# DB 테이블 생성
# =========================================================

def create_user_table():
    # 회원 정보를 저장할 userTable 생성
    conn, cur = connection()

    # 테이블이 없을 경우에만 생성
    # 이미 있으면 기존 테이블은 그대로 유지
    cur.execute("""
        CREATE TABLE IF NOT EXISTS userTable (
            id CHAR(20) PRIMARY KEY,
            pwd CHAR(20) NOT NULL,
            name CHAR(20) NOT NULL,
            email CHAR(20) NOT NULL,
            addr CHAR(50)
        )
    """)

    conn.commit()
    conn.close()


def create_board_table():
    # 게시글 정보를 저장할 boardTable 생성
    conn, cur = connection()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS boardTable (
            b_id BIGINT AUTO_INCREMENT PRIMARY KEY, -- 게시글 번호 자동 증가
            b_title VARCHAR(20) NOT NULL,            -- 제목
            b_text VARCHAR(1000) NOT NULL,          -- 내용
            writer CHAR(20) NOT NULL,               -- 게시글 작성자
            reg_date DATETIME DEFAULT CURRENT_TIMESTAMP, -- 작성시간 자동 등록

            -- 게시글 작성자는 실제 존재하는 회원이어야 함
            FOREIGN KEY (writer)
                REFERENCES userTable(id)
        )
    """)

    conn.commit()
    conn.close()


def create_comment_table():
    # 댓글 정보를 저장할 commentTable 생성
    conn, cur = connection()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS commentTable (
            C_num BIGINT AUTO_INCREMENT PRIMARY KEY, -- 댓글 번호 자동 증가
            C_number BIGINT NOT NULL,                -- 댓글이 작성된 게시글 번호
            C_writer CHAR(20) NOT NULL,              -- 댓글 작성자
            C_text VARCHAR(1000) NOT NULL,           -- 댓글 내용
            C_reg_date DATETIME DEFAULT CURRENT_TIMESTAMP, -- 댓글 작성시간

            -- C_number는 실제 존재하는 게시글 번호만 가능
            FOREIGN KEY (C_number)
                REFERENCES boardTable(b_id)
                ON DELETE CASCADE,

            -- C_writer는 실제 존재하는 회원 id만 가능
            FOREIGN KEY (C_writer)
                REFERENCES userTable(id)
        )
    """)

    # ON DELETE CASCADE
    # 게시글이 삭제되면 그 게시글에 달린 댓글도 같이 삭제됨

    conn.commit()
    conn.close()


# =========================================================
# 테스트용 초기 데이터
# =========================================================
def insert_sample_data():
    conn, cur = connection()

    # -------------------------
    # 기본 회원 데이터
    # -------------------------
    users = [
        ('ayj1234', '12345678', '안유진', 'ayj@gmail.com', '서울시 강남구'),
        ('jwy1234', '12345678', '장원영', 'jwy@gmail.com', '서울시 강남구'),
        ('fall1234', '12345678', '가을', 'fall@gmail.com', '서울시 강남구'),
        ('ys1234', '12345678', '이서', 'ws@gmail.com', '서울시 강남구'),
        ('lay1234', '12345678', '레이', 'lay@gmail.com', '서울시 강남구')
    ]

    # 기본 회원을 하나씩 확인
    for user in users:

        # user[0] = 회원의 id
        # 해당 id가 이미 DB에 존재하는지 먼저 검색
        cur.execute(
            "SELECT id FROM userTable WHERE id=%s",
            (user[0],)
        )

        # 검색 결과 1개를 가져옴
        row = cur.fetchone()

        # 검색 결과가 None이면 해당 회원이 없다는 뜻
        if row is None:
            # 없는 회원만 추가
            # 이미 존재하는 회원을 다시 INSERT해서 PK 중복 오류나는 것을 방지
            cur.execute(
                """
                INSERT INTO userTable(id, pwd, name, email, addr)
                VALUES(%s, %s, %s, %s, %s)
                """,
                user
            )

    # -------------------------
    # 기본 게시글 데이터
    # -------------------------

    # 현재 게시글이 몇 개인지 확인
    cur.execute("SELECT COUNT(*) FROM boardTable")
    board_count = cur.fetchone()[0]

    # 게시글이 0개일때만 기본 게시글을 넣음
    # 프로그램 실행할때마다 같은 게시글이 계속 추가되는것을 방지
    if board_count == 0:

        boards = [
            ('파이썬 질문입니다',
             '반복문을 공부하다가 궁금한 점이 생겼습니다.',
             'ayj1234'),

            ('MySQL 공부 중입니다',
             '외래키와 기본키의 차이를 공부하고 있습니다.',
             'jwy1234'),

            ('오늘 수업 정리',
             '오늘은 데이터베이스 CRUD에 대해 학습했습니다.',
             'fall1234'),

            ('게시판 테스트',
             '게시판 글 작성 기능을 테스트하고 있습니다.',
             'ys1234'),

            ('PyMySQL 질문',
             '파이썬에서 MySQL 연결 방법을 연습하고 있습니다.',
             'lay1234')
        ]

        for board in boards:
            # b_id와 reg_date는 자동으로 들어가기 때문에
            # 제목, 내용, 작성자 3개만 직접 INSERT
            cur.execute(
                """
                INSERT INTO boardTable(b_title, b_text, writer)
                VALUES(%s, %s, %s)
                """,
                board
            )

    # -------------------------
    # 기본 댓글 데이터
    # -------------------------

    # 현재 댓글이 몇 개인지 확인
    cur.execute("SELECT COUNT(*) FROM commentTable")
    comment_count = cur.fetchone()[0]

    # 댓글이 하나도 없을때만 기본 댓글 추가
    if comment_count == 0:

        comments = [
            (1, 'jwy1234', '저도 반복문 처음 배울 때 헷갈렸어요.'),
            (1, 'fall1234', 'for문과 while문을 비교해보면 이해하기 좋습니다.'),
            (2, 'ayj1234', '외래키는 다른 테이블과의 관계를 연결해주는 역할입니다.'),
            (3, 'ys1234', 'CRUD 정리 내용 잘 봤습니다.'),
            (5, 'lay1234', 'PyMySQL 연결 부분 저도 연습 중입니다.')
        ]

        for comment in comments:
            # C_num과 C_reg_date는 자동 등록
            # 게시글번호, 작성자, 댓글내용 3개만 INSERT
            cur.execute(
                """
                INSERT INTO commentTable(C_number, C_writer, C_text)
                VALUES(%s, %s, %s)
                """,
                comment
            )

    # INSERT한 내용을 DB에 실제 저장
    conn.commit()
    conn.close()


# =========================================================
# STEP 1. 회원가입
# =========================================================
def signup():
    conn, cur = connection()

    print("\n===== 회원가입 =====")

    # 아이디 중복 확인
    while True:
        user_id = input("아이디: ")

        # 입력받은 id가 DB에 존재하는지 검색
        cur.execute(
            "SELECT id FROM userTable WHERE id=%s",
            (user_id,)
        )

        # 검색 결과 하나를 가져옴
        row = cur.fetchone()

        # 결과가 있으면 이미 존재하는 id
        if row:
            print("이미 존재하는 아이디입니다.")

            # 다시 아이디 입력으로 돌아감
            continue

        # 중복이 아니면 while 종료 후 나머지 정보 입력으로 넘어감
        break

    user_pwd = input("비밀번호: ")
    user_name = input("이름: ")
    user_email = input("이메일: ")
    user_addr = input("주소: ")

    # 입력받은 회원 정보를 userTable에 저장
    cur.execute(
        """
        INSERT INTO userTable(id, pwd, name, email, addr)
        VALUES(%s, %s, %s, %s, %s)
        """,
        (user_id, user_pwd, user_name, user_email, user_addr)
    )

    conn.commit()
    conn.close()

    print("회원가입 완료!!")


# =========================================================
# STEP 2. 로그인
# =========================================================
def login():
    conn, cur = connection()

    print("\n===== 로그인 =====")

    user_id = input("ID 입력: ")
    user_pwd = input("PWD 입력: ")

    # 입력받은 ID와 PWD가 둘 다 일치하는 회원을 DB에서 검색
    cur.execute(
        """
        SELECT *
        FROM userTable
        WHERE id=%s AND pwd=%s
        """,
        (user_id, user_pwd)
    )

    # 로그인은 id가 PK라서 결과가 최대 1개
    # 그래서 fetchone() 사용
    row = cur.fetchone()

    conn.close()

    # 검색 결과가 있으면 로그인 성공
    if row:
        print("로그인 성공")

        # row 구조
        # [0] id / [1] pwd / [2] name / [3] email / [4] addr
        print(f"{row[2]}님 환영합니다.")

        # 로그인된 사용자 id를 반환
        # 이후 게시글/댓글 작성자와 권한 확인에 사용
        return user_id

    else:
        print("ID 또는 비밀번호가 일치하지 않습니다.")

        # 로그인 실패했으므로 로그인 사용자가 없음
        return None


# =========================================================
# STEP 3. 게시글 작성
# =========================================================
def write_post(current_user):
    # current_user = 현재 로그인한 사용자의 id
    # 제목/내용을 입력받고 writer에는 current_user를 저장할 예정
    pass


# =========================================================
# STEP 4. 게시글 목록 조회
# =========================================================
def list_posts():
    # boardTable과 userTable을 JOIN해서
    # 글번호 / 제목 / 작성자 이름 / 작성일을 출력할 예정
    pass


# =========================================================
# STEP 4. 게시글 상세 조회
# =========================================================
def view_post():
    # 게시글 번호를 입력받아서
    # 해당 게시글 본문 + 그 게시글에 달린 댓글을 출력할 예정
    pass


# =========================================================
# STEP 5. 댓글 작성
# =========================================================
def write_comment(current_user):
    # 먼저 입력받은 게시글 번호가 실제 존재하는지 확인
    # 존재하면 C_writer에 current_user를 넣어서 댓글 저장할 예정
    pass


# =========================================================
# STEP 6. 게시글 삭제
# =========================================================
def delete_post(current_user):
    # 삭제하려는 게시글의 writer를 먼저 확인
    # writer와 current_user가 같으면 본인의 글이므로 삭제
    # 다르면 다른 사람의 글이므로 권한 없음
    pass


# =========================================================
# 게시판 메뉴
# =========================================================
def board_menu(current_user):
    # login()에서 반환받은 로그인 사용자 id가 들어옴

    while True:

        print("\n===== 게시판 메뉴 =====")

        # 현재 누가 로그인되어 있는지 확인
        print(f"현재 로그인 사용자: {current_user}")

        print("1. 게시글 작성")
        print("2. 게시글 목록")
        print("3. 게시글 상세 조회")
        print("4. 댓글 작성")
        print("5. 게시글 삭제")
        print("6. 로그아웃")

        choice = input("메뉴 선택: ")

        if choice == "1":
            # 게시글 작성할때 현재 로그인 사용자도 같이 전달
            write_post(current_user)

        elif choice == "2":
            list_posts()

        elif choice == "3":
            view_post()

        elif choice == "4":
            # 댓글 작성할때도 현재 로그인 사용자 전달
            write_comment(current_user)

        elif choice == "5":
            # 본인의 게시글인지 확인해야 하므로 current_user 전달
            delete_post(current_user)

        elif choice == "6":
            print("로그아웃 합니다.")

            # 게시판 while문 종료
            # board_menu()가 끝나면서 다시 login_menu()로 돌아감
            break

        else:
            print("잘못된 입력입니다.")


# =========================================================
# 로그인 메뉴
# =========================================================
def login_menu():

    while True:

        print("\n===== 로그인 메뉴 =====")

        print("1. 로그인")
        print("2. 회원가입")
        print("3. 종료")

        choice = input("선택: ")

        if choice == "1":

            # login()의 반환값을 current_user에 저장
            # 성공 = 사용자 id / 실패 = None
            current_user = login()

            # 로그인에 성공해서 사용자 id가 있으면 게시판 메뉴로 이동
            if current_user:
                board_menu(current_user)

        elif choice == "2":
            signup()

        elif choice == "3":
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 입력입니다.")


# =========================================================
# 프로그램 시작
# =========================================================
if __name__ == "__main__":

    # 프로그램 실행시 테이블이 존재하는지 확인
    # 없으면 부모 → 자식 순서로 생성
    create_user_table()       # 1. 회원
    create_board_table()      # 2. 게시글
    create_comment_table()    # 3. 댓글

    # 테스트용 기본 데이터 등록
    # 이미 존재하는 데이터는 중복 등록하지 않도록 위에서 처리함
    insert_sample_data()

    # 테이블 준비가 끝났으면 로그인 화면부터 프로그램 시작
    login_menu()