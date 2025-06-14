input_count = int(input())

results = []
for i in range(input_count):
    H, W, N = map(int, input().split())
    result = ''
    cnt1 = 1

    while N > H:
        N -= H
        cnt1+= 1

    if cnt1 <= 9:
        result += str(N) + '0' + str(cnt1)
    else:
        result += str(N) + str(cnt1)

    results.append(result)

for s in results:
    print(s)