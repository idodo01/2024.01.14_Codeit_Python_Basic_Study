# 1. local variable (로컬 변수)
def my_function():
    x = 1 # 로컬 변수
    print(x)
    
my_function()

# print(x) 

# print(x)는 오류 발생
# x 는 로컬 변수이기 때문에

# 2. global variable (글로벌 변수)

y = 2 # 글로벌 변수

def my_function():
    print(y)

my_function()
print(y)

# 3. 로컬 변수와 글로벌 변수

z = 3 # 글로벌 변수

def my_function():
    z = 4 # 로컬 변수
    print(z)

my_function()
print(z)

# 4. 파라미터 또한 로컬변수

def square(x):
    return x * x
    
print(square(5))



