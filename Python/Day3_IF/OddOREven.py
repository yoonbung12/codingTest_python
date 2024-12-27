# EvenNumber

inputNumber = input("Select Number(1,2,......100)?")
divideNumber = input("insert the number?")

result = inputNumber % divideNumber
if result == 0:
    print(f"EvenNumber: {result}")
elif result == 1:
    print(f"OddNumber: {result}")