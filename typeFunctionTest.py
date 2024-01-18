# type() 타입을 알 수  있는 함수
print(type(3)) # int
print(type(3.0)) # float
print(type("3")) # str

print(type(True))  # bool
print(type("True")) # str


def hello():
    print("Hi")
    
print(type(hello)) # 함수
print(type(print)) # 내장함수