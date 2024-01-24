# 여기에 코드를 작성하세요


money = 50000000

apartment = 1100000000

year = 1988
YEAR_PERCENT = 1.12

while year < 2016 :
    money = money * YEAR_PERCENT
    year += 1


if apartment > money :
    print("{:.0f}원 차이로 미란 아주머니 말씀이 맞습니다.".format(apartment - money))
else :
    print("{:.0f}원 차이로 동일 아저씨 말씀이 맞습니다.".format(money - apartment))
    



