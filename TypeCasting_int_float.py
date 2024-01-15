#형변환, Type Conversion, Type Casting

# 숫자형 -> 숫자형
#int()
print(int(1.2))
#float()
print(float(1))

# 문자형 -> 숫자형
print(int("1")+int("2"))
print(float("1.1")+float("1.2"))


# 오류 뜨는 경우
# int() 함수는 오직 정수 형식의 문자열만을 인수로 받음
# print(int("1.1")) 
# print(int("hi"))

# (비교) float("정수")는 오류 안뜨고 정상출력됨
# print(float("1"))

