import random

friend = ["봉구","나나", "뽀솜", "호호", "설기"]

randomNumber = random.randint(0, 4)

if randomNumber == 0:
    print(friend[0])
elif randomNumber == 1:
    print(friend[1])
elif randomNumber == 2:
    print(friend[2])
elif randomNumber == 3:
    print(friend[3])
else:
    print(friend[4])

# 아니면 다른 방법 choice 함수 사용하기

print(random.choice(friend))