import random

RSP = ["바위", "가위", "보"]

print("가위 바위보 게임에 온것을 환영 합니다")

computerRSP = random.randint(0, 2)
print(computerRSP)

userRSP = input("가위 == 1, 바위 == 0, 보 ==2  셋중 하나를 넣으세요")

if computerRSP == int(userRSP):
    print("비겼습니다....")
elif computerRSP == 0  and int(userRSP == 1):
    print("컴퓨터 승")
elif computerRSP ==1 and int(userRSP == 2):
    print("컴퓨터 승")
elif computerRSP == 0 or int(userRSP == 2):
    print("유저 승")
elif computerRSP == 1 or int(userRSP == 2):
    print("컴 승")







