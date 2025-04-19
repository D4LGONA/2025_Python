n = []
for i in range(3):
    n = map(int, input().split())
    n = list(n)
    if n.count(0) == 0: print('E')
    elif n.count(0) == 1: print('A')
    elif n.count(0) == 2: print('B')
    elif n.count(0) == 3: print('C')
    else: print('D')

