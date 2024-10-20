# 첫째 줄에는 현재 시각이 나옴. 0 <= A <= 23
# 분 0 <= B <= 59 정수

# 두번째 줄에는 요리하는데 필요한 시간 C 분 단위

H, M = map(int, input().split())
CookTime = int(input())

H += CookTime // 60
M += CookTime % 60

if(M >= 60):
    M -= 60
    H += 1

if(H >= 24):
    H -= 24

print(H, M)
