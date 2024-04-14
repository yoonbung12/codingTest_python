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
f = "I eat {0} bananas" .format(3)
print(f)