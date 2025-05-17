n, k = map(int, input().split())
arr = []

max = 0
for i in range(1, k + 1):
    tmp = int((str(i * n))[::-1])
    if max < tmp:
        max = tmp

print(max)
