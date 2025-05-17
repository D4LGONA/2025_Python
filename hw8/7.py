cnt = int(input())
lst = set()

for _ in range(cnt):
    tmp = input().split()
    if tmp[1] == "enter": lst.add(tmp[0])
    else: lst.discard(tmp[0])

for name in sorted(lst, reverse=True):
    print(name)