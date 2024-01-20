def print_square(x):
    print(x * x)

def get_square(x):
    return x * x

# 4
print_square(2)
# 아무것도 출력되지 않음
get_square(2)

# 파이썬에서는 
# print안에 함수의 리턴 값이 없을 경우
# None를 출력해준다

# 9
# None
print(print_square(3)) 

# 9
print(get_square(3))
