# for 문
test_list = ["one", "two", "three"]

for i in test_list:
    print(i)

a = [ (1,2), (3,4), (5,6)]

for (first, last) in a:
    print (first + last)

#  for문 실질적인 예시
marks = [90, 25, 67, 30, 44] # 학생들 시험 점수 리스트

number = 0 # 학생에게 붙여줄 번호

for mark in marks:
    number += 1
    if mark >= 60:
        print("%d번 학생의 점수는 합격입니다." % number)
    else:
        print("%d번 학생은 불합격 입니다...ㅠㅠ" % number)

# for문과 함께 쓰는 continue와 range함수
add = 0
for i in range(1, 11):
    add = add + i
    print(add, end= " ")

# 활용 방법 좋은 예시
b = [1,2,3,4]
result = [num * 3 for num in b if num % 2 == 0]
# 풀어서 작성하면 
#  result = []
#  for num in b
#      if num % 2 == 0:
#          result.append(num * 3)
print(result)
