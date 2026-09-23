# Pandas: 테이블 형태의 데이터를 쉽게 다룰 수 있도록 설계된 파이썬 데이터 분석
# 데이터 전처리, 탐색, 변환 및 시각화 등의 작업에 널리 사용
# 행과 열의 구조로 구성된 데이터를 직관적으로 다룰 수 있게 해줌

# - Series(1차원), DataFrame(2차원) 구조 지원
# - 다양한 데이터 파일(CSV, Excel, SQL, JSON 등) 불러오기 가능
# - 결측치 처리, 정렬, 그룹화, 필터링, 통계 분석 등 풍부한 기능 제공
# - 시계열 데이터 처리 기능 내장

"""
- **데이터 분석 및 통계 처리**
- **머신러닝 전처리** (scikit-learn과 함께 사용)
- **금융 및 투자 분석** (주가, 수익률 분석 등)
- **마케팅/CRM 데이터 분석**
- **공공데이터/IoT 시계열 분석**
- **웹 로그, 사용자 행동 분석** 등
"""

import pandas as pd

# Series - 1차원 데이터 구조: 리스트와 유사하지만, 각 데이터에 인덱스(라벨)이 부여됨
# 1차원은 실제로 잘 안쓰임 판다스에서
s1 = pd.Series([10,20,30,40,50,60])
print(s1)

# DataFrame - 2차원 DataSet : 여러 개의 Series가 모여 이루어지며, 행과 열로 구성됨
data = {
    '이름': ['민지','규석','철수','유리'], # 세로
    '수학': [95, 85, 75, 50],
    '영어': [90, 88, 94, 70]
}
df = pd.DataFrame(data)
print(df)
print("=======")

# 특정 '행' 및 '열' 추출
print(df['수학']) # 열 추출
print("===구분선====")
print(df.loc[0]) # 행 추출  인덱스 부분
print("===구분선====")
print(df.loc[1,'영어']) # 1번 인덱스에 영어인 값 88


# 새로운 열 및 행 추가
df['과학'] = [93,89,87,20] # 새 열 추가
df.loc[4] = ['혜인',92,89,77]
print(df)

# 기본 연산
print(df['수학'].sum())  # 합계,평균,최대,최소값
print(df['수학'].mean())
print(df['수학'].max())
print(df['수학'].min())

# 열 추가
df['반'] = [1,1,2,2,3]
print(df)

print(df.groupby('반')['수학'].mean().rename("수학평균"))


# 문제
print("문제 경계선")
ef = pd.read_csv("exam.csv")
print(f"전체 행 개수: {len(ef)}")

# 2번
print(ef['math'])

# 3번
print(ef['math']>=80)

# 4번
print(f"영어 평균점수: {ef['english'].mean()}")

# 5번
# new_ef = pd.write_csv("exam.csv")
ef.to_csv("filtered_exam.csv", index=False)

# 6번
print(ef.groupby('nclass')[['math','english']].mean())

#7번
print(ef.groupby('nclass')['math'].agg([max,min]))

# 8qjs
data_fruit = {
    '제품': ['사과','딸기','수박'], # 세로
    '가격': [1800, 1500, 3000],
    '판매량': [24, 38, 13]
}
data_fruit= pd.DataFrame(data_fruit)
print(data_fruit)
print("=======")