# import 모듈과패키지
# # from 모듈과패키지 import *
#
# print(모듈과패키지.add(1000,2000))
# print(add(1000,2000))

"""
파이썬에서 예외처리(Exception Handling)는 프로그램 실행 중에 발생할 수 있는 오류를 적절히 
처리하여 프로그램이 비정상적으로 종료되지 않도록 하는 방법입니다. 
예외 처리는 주로 try, except, else, finally 블록을 사용하여 처리합니다.
"""

"""
`try:`
예외가 발생할 가능성이 있는 코드`

except:
예외가 발생했을 때 실행할 코드`

else:
예외가 발생하지 않았을 때 실행 할 코드`

finally:
무조건 실행하는 코드
"""
while True:
    try:
        print("나눗셈 계산기 입니다.")
        num1= int(input("첫 번째 숫자 입력: "))
        num2= int(input("두 번째 숫자 입력: "))
        print(f"{num1} / {num2} = {int(num1/num2)}")
    except ValueError:
        print("에러!! 잘못된 값을 입력 하였습니다.")
        continue
    except ZeroDivisionError as err:
        print(err)
        continue
    except Exception as err:
        print(err)
        continue
    else:
        print("정상 처리 되었습니다.")
        break
    # finally:
    #     print("프로그램 실행 완료!!")
print("프로그램 실행 종료")



