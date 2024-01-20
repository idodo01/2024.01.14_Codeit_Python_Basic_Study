def first():
    message = "코드잇"
    return message
    
def second():
    message = "codeit"
    print(message)

def third():
    message = "None1"
    print(message)
    

# 테스트 코드
print(first())
second()
print(third())  

# print안에 함수의 리턴값이 없을 경우
# None 출력됨

# 코드잇    -   print(first())의 first()리턴값 출력됨
# codeit    -   second()의 print(message)가 출력됨
# None1      -   print(third())의 third()의 print(message) 출력됨
# None      -   print(third())의 third()가 리턴값이 없어서 출력됨 
        
