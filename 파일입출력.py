# 파일 입출력


# 파일 쓰기
# score_file = open("score.txt", "w", encoding="utf-8") # w 쓰기 모드

# print("수학 : 30", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.write("과학 : 80" + "\n")
# score_file.write("코딩 : 100" + "\n")
# score_file.close()


# 파일 읽기
score_file = open("score.txt", "r", encoding="utf-8") # r이 읽기 모드
print(score_file.read()) # 파일 전체의 내용을 열어서 하나의 문자열로 반환
score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
while True:
    line = score_file.readline() # 한 라인씩 문자열로 만들기
    if not line:
        break
    print(line, end="")
score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
lines = score_file.readlines() # 모든 행을 읽어서 리스트로 만듬
for line in lines:
    print(line, end="")
score_file.close()


#  with 구문
#  with 구문을 사용하게 되면 구문이 종료 될 때 자동으로 파일이 닫힙니다
with open('score.txt', 'r', encoding="utf-8") as score_file:
    content = score_file.read()


