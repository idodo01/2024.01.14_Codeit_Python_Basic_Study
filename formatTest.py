# 오늘은 2024년 1월 18일입니다.
year = 2024
month = 1
day = 18

# str 과 int 값을 합칠 수 없음
# print("오늘은"+year+"년 "+month+"월 "+day+"일입니다.")

# int값을 str로 변환한 후 합칠 수 있음
print("오늘은 "+str(year)+"년 "+str(month)+"월 "+str(day)+"일입니다.")

# .format() 사용하여 문자열 포맷팅
print("오늘은 {}년 {}월 {}일입니다.".format(year,month,day))
