n = int(input())

ls = [list(map(int, input().split())) for _ in range(n)]
res = []

ls.sort(key=lambda x: (x[1], x[0]))

count = 0
end_time = -1
for j in range(n):
    if ls[j][0] >= end_time:
        count += 1
        end_time = ls[j][1]

print(count)