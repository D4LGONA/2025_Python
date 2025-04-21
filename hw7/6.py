from random import *
data = []
i, k = 0, 0

if __name__ == '__main__':
    for i in range(10):
        tmp = hex(randrange(0, 100000))
        data.append(tmp)
    print('정렬 전 데이터: ', end = "")
    [print(num, end = ' ') for num in data]
    print()

    for i in range(len(data)-1):
        for k in range(i + 1, len(data)):
            if int(data[i], 16) > int(data[k], 16):
                data[i], data[k] = data[k], data[i]

    print('정렬 후 데이터: ', end="")
    [print(num, end=' ') for num in data]