s = input("숫자를 여러 개 입력하세요: ")

for i in s:
    for j in range(int(i) * 2):
        print("★", end='')
    print()