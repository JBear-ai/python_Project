# Numpy (Numerical) 파이썬에서 수치 계산과 과학적 연산을 위한 핵심 라이브러리입니다.
# 데이터의 언어는 '숫자'와 '행렬'이며 이를 효율적으로 처리 하기 위해 Numpy를 사용
# 빅데이터 환경에서 파이썬 기본 리스트로 반복문을 돌리는 것은 매우 느림
# 너마이의 벡터화 연산을 쓰면 수백만 개의 데이터를 순식간에 처리 가능
# 대규모 다차원 배열 처리
# 고속 수학 연산 지원
# 머신러닝, 딥러닝, 데이터 분석에서 필수적으로 사용 함

import numpy as np

# 기본 배열 생성
data = [0,1,2,3,4,5]
a1 = np.array(data) # 리스트를 넘파일 배열로 만듬
print(data)
print(a1)

data2 = [0,1,2,3,4.4,5.14,6.75] # 하나의 타입으로 통일
a2 = np.array(data2)
print(a2)

# 문자열, 실수, 정수를 포함하는 배열을 만들어서 출력 결과
data3 = [0,1,2,3,4,5.14,6.75,"실수형","정수형"]
a3 = np.array(data3)
print(a3)

data4 = [0,1,2,3,4,"실수형","정수형",5.14,6.88]
a4 = np.array(data4)
print(a4)

# 속성 확인
x =np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8]) # 8개
print(x)
print(x.shape) # 배열의 형태를 나타냄
print(x.dtype) # 요소의 데이터 타입 변환


# 특정 범위의 배열 생성
a5=np.arange(0, 10,2) # 0에서 10미만 까지 범위 지정 간격은 2정도
print(a5)

a6=np.arange(1, 101, 3)
print(f"{a6}\n")

a7=np.arange(0, 50, 5)
print(a7)
print()

# 2차원 배열 생성
a8=np.arange(12).reshape(4,3) # 0부터 12미만이며 4행 3열로 2차원
print(a8)
print(a8.shape)

# 동일한 간격으로 데이터 생성
a9 = np.linspace(1,10,11) # 1과 10사이에
print(a9)

# NumPy 기초
# 1번
print("-----------------------")
arr1 = [10,20,30,40,50]
arr1_np = np.array(arr1)
print(arr1_np)
print(type(arr1_np))
print(arr1_np.shape)
print(arr1_np.dtype)
print("------------------------")
# 2번
arr_data = ["True",1,2]
print(arr_data)


print("------------------------")
#3번
arr8=np.array([[1,2,3],[4,5,6]])
# arr8 = np.arange(1,7).reshape()
print(arr8.shape)
print(arr8.dtype)

#4번
arr9 = np.arange(2,21,2)
print(arr9)
#5번
arr10 = np.arange(10,0,-1)
print(arr10)

arr11 = np.arange(0,1,0.1)
print(arr11)
print(len(arr11))

# 특정 숫자로 채워진 배열
print("============")
b1 = np.zeros(10) #
print(b1)

b2 = np.zeros((3,4))
print(b2)

b3 = np.ones(10)
print(b3)

b4 = np.eye(4)
print(b4)

# 배열의 데이터 타입 변환
b5 = np.array(['1.5', '0.62', '2', '3.14', '3.141592'])
print(b5)
print(b5.dtype) # <U8의 의미는 데이터 형식이 유니코드이며 문자의 수는 최대 8자

num_b5= b5.astype(float) # 문자열을 실수 타입으로
print(num_b5)

b6 = np.array(['1', '3', '5', '7', '9']) # 문자열을 정수 타입으로
num_b6 = b6.astype(int)
print(num_b6)

# 난수 배열의 생성 (랜덤)
# rand() : 0~1 미만의 실수로 난수 배열을 생성
b7 = np.random.rand(2,3) # 2차원 배열
print(b7)
b8 = np.random.rand(2, 3, 4) # 3 차원 배열
print(b8)

# randint() : 지정된 범위에 해당하는 정수로 난수 배열
b9 = np.random.randint(10, size=(3, 4)) # 0 ~ 9 사이의 정수
print(b9)

# 실습 문제 2
# 1
print("실습시작부분")
c1 = np.zeros(5)
print(c1)
print(c1.dtype)
print()

# 2
c2 = np.zeros((3,5))
print(c2.shape)
print()

# 3
c3 =np.ones((2,4))
num_c3 = c3.astype(int)
print(num_c3)
print()
#4
print("중간 점검")
c4 = np.eye(5)
print(c4)

#5
print()
c5 = np.array(['10','20','30','40'])
num_c5 = c5.astype(int)
print(num_c5)
print(f"타입은:{num_c5.dtype}")

#6
print()
c6 = np.random.rand(4,3)
print(c6)
print(c6.shape)

#7
print()
c7 = np.random.randint(1,7,10)
print(c7)

#8
print()
c8 = np.random.randint(0,100,12)
print(c8)

c8 = c8.reshape((3,4))
c8 = c8.astype(float)
print(c8)
print(c8.shape)
print(c8.dtype)

# 연산과 함수
# d1 = [1,2,3]
# d2 = [4,5,6]
d1 = np.array([1,2,3])
d2 = np.array([4,5,6])
print(d1+d2) # 각 요소별로 연산함  [5 7 9]
print(d1*d2)
print(d1/d2)

d3 = np.array([10,20,30,40,50])
print(d3>20) # TRUE, FALSE로 반환

# 통계 연산
d4 = np.arange(10)
print(f"합계 : {d4.sum()}, 평균 : {d4.mean()}")
print(f"표준편차 : {d4.std()}, 분산 : {d4.var()}")
print(f"최솟값 : {d4.min()}, 최댓값 : {d4.max()}")


# 문제1
e1 = np.arange(1,11)
total_e1 = e1+5
print(total_e1)

# 문제2
e2 = np.arange(1,10).reshape(3,3)
print(e2)
print(e2.shape)

# 문제3
e3 = np.arange(1,21)
print(f"합계 : {e3.sum()}, 평균 : {e3.mean()}")
print(f"최솟값 : {e3.min()}, 최댓값 : {e3.max()}")

# 문제4
e4 = np.random.randint(0,101,size=(10))
print(e4[e4>=50])
print(e4.dtype)
# if e4 >= 50:
#     print(e4)