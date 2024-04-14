print("hello world")
# 문자열 더하기
head = "python"
tail = "is fun"
print(head + tail)

# ===글자 갯수 구하기=======
a  = "sdfo wker ㄴㅇㄹㄴㄴㅇㄹㅇㄴ  klwen"
print(len(a))
print(a[1])
# a[ 이상 : 미만 : 간격]
b = "20240414Sunny"
date = b[:8]
weather = b[8:]
print(date)
print(weather)
print(date + weather)

# 숫자나 문자 넣어주기
food = "김치"
number = 3
c = "나는 %s을  먹었다. " % food  # %s는 뭐든지 바꿔서 넣어줄수 있다.
d = "바나나를 %d개 먹었다." % number
print(c)
print(d)

# 소수점 표현하기
e = "%0.4f" % 3.1235323 # 소수점 넷째자리까지 표현해라
print(e)

# format
f = "I eat {0} bananas , so i tired {1}days" .format("five", 3) # .format(3) 숫자로 넣어도 상관 없다.
print(f)
# 3.0이상부터는 f를 붙이면 됨
name = "봉구"
age = 29
g = f"my name is {name} and {age}살 이다"
print(g)

# join
h = " to the ".join(['a', 'b', 'd', 'e']) #("abcd")
print(h)

# split(띄어쓰기)
i = "Life is too short"
print(i.split())

# 리스트****** ===== del(지우기), 정렬은 sort사용, [pop(꺼내기),append(추가)], reverse등등 좀 외워 둘것. =====
j = [ 0, 1, 2 ,["a", "b", "c"]]
print(j[3])
print(j[-1][2])

k = [1,2,3]
print(j + k) # 3 * k 곱하기도 가능**