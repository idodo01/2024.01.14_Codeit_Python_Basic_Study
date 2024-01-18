# 문자열 출력
print("저는 {} {} {}를 좋아합니다".format("사과","바나나","포도"))

# 문자열 순서 정해서 출력
# 인덱스는 0부터 시작
print("저는 {2} {1} {0}를 좋아합니다".format("사과","바나나","포도"))


num1 = 1
num2 = 3

# 숫자 출력
print("{0} 나누기 {1}은 {2}입니다".format(num1,num2,num1/num2))
# 숫자 반올림 출력
print("{0} 나누기 {1}은 {2:.0f}입니다".format(num1,num2,num1/num2))
print("{0} 나누기 {1}은 {2:.2f}입니다".format(num1,num2,num1/num2))