n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))
count = 0
for i in range(len(coins) - 1, -1, -1):
    if k >= coins[i]:
        count += k // coins[i]
        k %= coins[i]

print(count)