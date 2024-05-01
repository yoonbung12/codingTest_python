# 오큰수 구하기 백준 17928(스택)
n = int(input())
ans = [0] * n
A = list(map(int, input().split))
myStack = []

for i in range(n):
    while myStack and A[myStack[-1]]:
        