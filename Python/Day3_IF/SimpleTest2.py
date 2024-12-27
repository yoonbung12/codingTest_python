# 피쟈 IF문...테스트
size = input("What do you want to choice your Pizza Size? S Or M Or L:")
peperoni = input("If you want to add peperoni?? Y OR N:")
extra_cheese = input("If you want to add cheese?? Y OR N:")

# 총 피자 금액
totalPrice = 0

if size == "S":
    print("S의 가격은 4$입니다.")
    sizePrice = 4
elif size == "M":
    print("M의 가격은 7$입니다.")
    sizePrice = 7
else:
    sizePrice = 12

    if peperoni == "Y":
        peperoniPrice = 4
    else:
        peperoniPrice = 0

    if extra_cheese == "Y":
        addCheesePrice = 5
    else:
        addCheesePrice = 0

    totalPrice = sizePrice + peperoniPrice + addCheesePrice
    print(f"총 가격은 {totalPrice}$ 입니다.")


