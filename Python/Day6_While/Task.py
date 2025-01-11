# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def move_to():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
#
# for step in range(6):
#     move_to()
#
# numberOfHudle = 6
# while numberOfHudle > 0:
#     move_to()
#     numberOfHudle -= 1
#     print(numberOfHudle)
while at_goals() != True:
    move_to()