print("Welcome to the tip calculator")

payMoney = float(input("What was total bill??"))

tipMoney = int(input("How much tip would you like to give? 10, 12. Or 15?"))

howManyPeople = int(input("How many people to split the bill??"))

EachPersonPayMoney = tipMoney / 100 * payMoney + payMoney

print(EachPersonPayMoney)

Each_pay = EachPersonPayMoney / howManyPeople
print(f"Each people pay the ${Each_pay}")