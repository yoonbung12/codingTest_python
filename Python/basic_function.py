# 함수의 구조
#  **초기화 하고 싶은 매개변수는 항상 뒤에 나둬야 한다.
# def add(a,b):
#     return a + b

# print(add(1,2))

# def sub(a,b):
#     return a - b

# result = sub(a= 7, b =1) # a에 7, b에 3
# print(result)

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul("mul", 1,2,3,4)
print(result)

def say_nick(nickname):
    if nickname == "stupid":
        return "이 바보야!!"
    else:
        print("나의 별명은 %s 입니다." % nickname)

say_nick("하하하")
say_nick("stupid")

# 사용자 입출력 
number = input("숫자를 입력하세요")

print("number = %s 입니다" % number)