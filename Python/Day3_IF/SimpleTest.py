weight = 85
height = 1.85

bmi = float(weight / (height ** 2))

if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi < 25:
    print("normal weight")
else:
    print("너는 돼지야...")