# 구간합 2 백준(11659번)
import sys
input = sys.stdin.readline



# 숫자 갯수N, 질의갯수 M
n, m = map(int, input().split())

# 넣어야할 숫자들 원본배열에다가(numbers)
numbers = list(map(int, input().split()))
sumArr = [0] # 합배열 index시작을 1로 하기 위해서 0을 집어 넣음.
sum = 0

# 숫자 갯수 만큼 반복하기
for i in range(n):
    sum = sum + numbers[i] #합 배열에 넣을 값
    sumArr.append(sum)

# 질의 갯수
for i in range(m):
    i, j = map(int, input().split())
    print(sumArr[j] - sumArr[i -1])

