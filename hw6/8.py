a = eval(input())
for i in range(a):
    for j in range(a):
        if i + j < a - 1: print(" ", end="")
        else: print("*", end="")
    print("")