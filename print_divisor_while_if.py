# 여기에 코드를 작성하세요

n = 120
i = 1
count = 0

while i <= 120 :
    if n % i == 0 :
        print(i)
        count += 1
    i += 1
        
print(f"{n}의 약수는 총 {count}개 입니다.")