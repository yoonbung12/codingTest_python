# 롤러코스터 탈수 있는 나이 및 키 높이
height = int(input("What is your height???"))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int((input("how old are you?")))
    if age <= 12:
        print("You Should pay the 5$")
    else:
        print("you Should pay the 12$")
else:
    print("You can't ride the rollercoaster")