score = 65

# if else 으로만 코드를 작성하면
# 조건이 많아질 수록 복잡해진다
if score >= 90 :
    print("A")
else :
    if score >= 80 :
        print("B")
    else :
        if score >= 70 :
            print("C")
        else :
            if score >= 60 :
                print("D")
            else : 
                print("F")
# elif를 사용하여 간단하게
# 다양한 조건이 포함된 if문을 작성할 수 있다

if score >= 90 :
    print("A")
elif score >= 80 :
    print("B")
elif score >= 70 :
    print("C")
elif score >= 60 :
    print("D")
else : 
    print("F")
                