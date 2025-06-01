import sys
input = sys.stdin.readline

s = set()

n = int(input())
for _ in range(n):
    ls = input().split()
    tmp = ls[0]
    if len(ls) > 1:
        i = int(ls[1])
    if tmp == 'add':
        s.add(i)
    elif tmp == 'remove':
        if i in s:
            s.remove(i)
    elif tmp == 'check':
        if i in s: print('1')
        else: print('0')
    elif tmp == 'toggle':
        if i in s: s.remove(i)
        else: s.add(i)
    elif tmp == 'all':
        s = { 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 }
    else:
        s.clear()