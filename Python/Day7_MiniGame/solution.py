import random
word_List = ["apple", "mango", "watermelon", "strawberry", "kiwi", "melon"]

lives = 6
chosenWord = random.choice(word_List)
print(chosenWord)

# ToDo1 placeHolder
placeHolder = ""
word_Length = len(chosenWord)
for position in range(word_Length):
    placeHolder += "_"
print(placeHolder)



# Todo2: Create "display"


# 게임이 끝나는 경우를 만들어 놓기
game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    # 맞았을 경우 또한번 질문을 하도록 만들어야한다...
    for letter in chosenWord:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
            # print("Right")
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
            # print("Wrong")

    print(display)

    # If 추측한 스펠링이 틀릴경우
    if guess not in chosenWord:
        lives -= -1
        if lives == 0:
            game_over = True
            print("너 졌어 ㅋㅋㅋㅋ")



    if "_" not in display:
        game_over = True
        print("너가 이김ㅋㅋㅋㅋㅋㅋㅋ")



