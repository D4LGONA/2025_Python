l = ["" for i in range(8)]

for i in range(8):
    l[i] = input()

cnt = 0

for i in range(8):
    for j in range(8):
        if i % 2 == 0:
            if j % 2 == 0 and l[i][j] == 'F':
                cnt += 1
        else:
            if j % 2 != 0 and l[i][j] == 'F':
                cnt += 1

print(cnt)
