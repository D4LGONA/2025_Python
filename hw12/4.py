res = [False] * 30

for i in range(28):
    n = int(input())
    res[n-1] = True

for i in range(len(res)):
    if res[i] == False:
        print(i+1)