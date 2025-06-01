n = int(input())
young = []
old = []

for i in range(n):
    tmp = input().split()
    if len(young) == 0 and len(old) == 0:
        young = [tmp[0], int(tmp[1]), int(tmp[2]), int(tmp[3])]
        old = [tmp[0], int(tmp[1]), int(tmp[2]), int(tmp[3])]
    if young[3] < int(tmp[3]) or (young[3] == int(tmp[3]) and young[2] < int(tmp[2])) \
        or (young[3] == int(tmp[3]) and young[2] == int(tmp[2]) and young[1] < int(tmp[1])):
        young = [tmp[0], int(tmp[1]), int(tmp[2]), int(tmp[3])]
    if old[3] > int(tmp[3]) or (old[3] == int(tmp[3]) and old[2] > int(tmp[2])) \
        or (old[3] == int(tmp[3]) and old[2] == int(tmp[2]) and old[1] > int(tmp[1])):
        old = [tmp[0], int(tmp[1]), int(tmp[2]), int(tmp[3])]

print(young[0])
print(old[0])