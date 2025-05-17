a, b = map(int, input().split())
s1 = set()
s2 = set()

for _ in range(a):
    s1.add(input())
for _ in range(b):
    s2.add(input())

s3 = s1.intersection(s2)
print(len(s3))
for s in sorted(s3):
    print(s)