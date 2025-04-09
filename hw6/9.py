a = int(input())

# i == 0일때 6, 7
# i == 10일때 6, 7

if a % 2 == 0:
    for i in range(a * 2 - 1):
        for j in range(a * 2):
            if a + i + 1 > j >= a - i - 1 or a + i + 1 > j >= a - i - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
