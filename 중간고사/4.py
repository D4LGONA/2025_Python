a, b = input().split()
arr = [['.' for _ in range(len(a))] for _ in range(len(b))]

flag = False
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            for k in range(len(a)):
                arr[j][k] = a[k]
            for k in range(len(b)):
                arr[k][i] = b[k]
            flag = True
            break
    if flag: break

for a in arr:
    for c in a:
        print(c, end="")
    print()