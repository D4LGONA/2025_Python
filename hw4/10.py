a, b, c = map(int, input().split())
s = int(input())

t = c + b * 60 + a * 3600 + s
a = (t // 3600) % 24
b = (t // 60) % 60
c = t % 60

print("%d %d %d" %(a, b, c))