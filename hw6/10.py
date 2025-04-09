a = eval(input())
b = eval(input())

min = 0
sum = 0
if a == 1: a = 2
for i in range(a, b + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        if min == 0: min = i
        sum += i
else:
    if min == 0: print(-1)
    else:
        print(sum)
        print(min)