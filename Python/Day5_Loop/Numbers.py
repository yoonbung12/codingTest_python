student_Score = [15, 20, 30, 100, 50, 120, 15]

sum = 0

for score in student_Score:
    sum += score

print(f"sum == {sum}")

# max_score 찾기
max_score = 0

for score in student_Score:
    if score > max_score:
        max_score = score
        # print(max_score)

print(f"max_score는 {max_score}다")