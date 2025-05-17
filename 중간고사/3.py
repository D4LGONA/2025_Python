n = eval(input())

for i in range(n):
    for j in range(n, 0, -1):
        if j <= i + 1: print(j, end="")
        else: print(".", end="")
        print(" ", end="")
    for j in range(1, n):
        if j < i + 1:
            print(j + 1, end="")
        else:
            print(".", end="")
        if j != n-1 : print(" ", end="")
    print()
