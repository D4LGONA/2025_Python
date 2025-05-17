def addNumber(num):
    if num == 1:
        return 1
    else:
        return num + addNumber(num - 1)

print(addNumber(100))
