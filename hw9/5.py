
def palindrom(s, n1, n2):
    global count
    count += 1
    if n1 >= n2: return 1
    elif s[n1] != s[n2]: return 0
    else: return palindrom(s, n1+1, n2-1)

n = int(input())

for i in range(n):
    count = 0
    s = input()
    print(palindrom(s, 0, len(s) -1), count)
