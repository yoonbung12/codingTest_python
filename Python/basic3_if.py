# if문
from operator import truediv
from pickle import TRUE


money = True
if money: # if뒤에 조건문 쓰면 됨 그리고 else if == elif
    print("택시를 타고가자")
else:
    print("걸어가라")

# else if문
bill = 3000
if bill >= 4000:
    print("택시 타고 가고")
else:
    print("택시는 무슨 걸어가!!!")


pocket = ['paper', 'cellphone', 'money']
card = True
if 'mmm' in pocket:
    print("택시 ㄱㄱㄱ")
elif card:
    print("택시 타자 카드있어")
else:
    print("택시는 무슨 걸어...")

# if 'money' in pocket:
#     pass # true여도 print 찍고 싶지 않을때 pass 사용
# else:
#     print("아니 존재하지 않아...")

# in, not in
print(1 in [1,2,3])
print(1 not in [1,2,3])

# while문
treeHit = 0
while treeHit < 10:
    treeHit += 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 11:
        print("나무가 꺾였습니다.")

# prompt = """
# 1. ADD
# 2. DEL
# 3. LIST
# 4. QUIT
# ENTER number: """

# number = 0
# while number != 4:
#     print(prompt)
#     number = int(input())

coffee = 10
money1 = 3000
while money1:
    print("커피를 시켜먹습니다.")
    coffee -= 1
    print("남은 커피의 양은 %d 입니다." % coffee)
    if coffee == 0:
        print("SOLD OUT")
        break