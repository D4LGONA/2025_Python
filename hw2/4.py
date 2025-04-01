a = eval(input())
b = input()
b = b[::-1]

cnt = 0
for s in b:
    tmp = int(s)
    print(tmp * a)
    cnt += 1
b = b[::-1]
print(a * int(b))