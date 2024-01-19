# return문의 역할
# 1. 값 돌려주기
# 2. 함수 즉시 종료하기


def square(x):
    print("함수 시작")
    return x * x
    print("함수 종료") # Dead Code (의미없는 코드
    )

print(square(3))
print("Hello")