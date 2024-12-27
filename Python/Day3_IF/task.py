# 롤러코스터 탈수 있는 나이 및 키 높이
height = int(input("What is your height???"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int((input("how old are you?")))
    if age <= 12:
        bill = 5
        print("You Should pay the 5$")
    elif age <= 18:
        bill = 7
        print("you Should pay the 7$")
    else:
        bill = 12
        print("Adult ticket price is 12$")

    wants_photo = input("Do you take a photo?? Y OR N ")
    if wants_photo == "Y":
        bill = bill + 3

    print(f"your pay the {bill}$")
else:
    print("You can't ride the rollercoaster")