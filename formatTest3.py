name = "최지웅"
age = 32

# 가장 오래된 방식 (% 기호)
print("제 이름은 %s이고 %d살입니다." % (name, age))

# 현재 가장 많이 쓰는 방식(2020년 2월 기준) (format() 메소드) 
print("제 이름은 {}이고 {}살입니다.".format(name, age))

# 새로운 방식 (f-string)
print(f"제 이름은 {name}이고 {age}살입니다.")