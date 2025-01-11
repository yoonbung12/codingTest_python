import random
WordList = ["apple", "banana", "kiwi", "mango", "watermelon"]

# 1번 랜덤한 값을 뽑기
keyword = random.choice(WordList)
print(keyword)

# keyword의 갯수만큼 "_" 찍어내기
wordLength = len(keyword)
wordBar = ("_" * wordLength)


# 3번 유저에게 질문하기
userInput = input(f"글자의 갯수는 {wordBar}야 한번 맞춰봐!!").lower()


for i in range(wordLength):
    if keyword == userInput:
        print("정답 입니다~~")
        
    else:
        print("틀렸어 다시 적어")


