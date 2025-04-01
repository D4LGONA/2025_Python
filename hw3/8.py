s = ''

if __name__ == '__main__':
    s = input("문자열을 입력-->")
    #print(s[::-1])
    for i in range(len(s) - 1, -1, -1):
        print('%c' %s[i], end='')
