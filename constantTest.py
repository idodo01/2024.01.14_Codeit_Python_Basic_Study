# 상수 (constant) : 바뀌지 않는 값
# 상수명은 모두 대문자로 작성하여 표기

PI = 3.14 # 원주율 '파이'

# 반지름을 받아서 원의 넓이 계산
def calculate_area(r):
    return PI * r * r 

radius = 4 # 반지름
print("반지름이 {}면, 넓이는 {}".format(radius,calculate_area(radius)))

# PI = 0 
# 상수도 값을 바꿀 수는 있지만,
# 그러면 좋지 못한 코드이다.

radius = 5 # 반지름
print("반지름이 {}면, 넓이는 {}".format(radius,calculate_area(radius)))
