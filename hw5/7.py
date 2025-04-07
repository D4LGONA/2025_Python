n = int(input())
for i in range(n):
    l = input().split()
    ans = float(l[0])
    for c in range(1, len(l)):
        if l[c] == "@":
            ans *= 3
        elif l[c] == "%":
            ans += 5
        elif l[c] == "#":
            ans -= 7
    print("%.2f" % ans)  # 출력: 3.14
