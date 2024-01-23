# 여기에 코드를 작성하세요


num = 1
sum = 0

while num < 1000 :
    if num % 2 == 0 :
        sum += num
    if num % 3 == 0 :
        sum += num
    if num % 6 == 0 :
        sum -= num

    # OR 을 사용한 코드
    # if num % 2 == 0 or num % 3 == 0:
    #    sum += num
        
    num += 1
    
print(sum)
        
