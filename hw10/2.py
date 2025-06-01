s = []

maxLen = 0
for i in range(5):
    s.append(input())
    if len(s[-1]) > maxLen:
        maxLen = len(s[-1])

for i in range(maxLen):
    for j in range(5):
        if len(s[j]) <= i: continue
        print(s[j][i], end='')