a = int(input())

for i in range(1, a + 1):
    for j in range(a - i):
        print(' ', end='')
    for j in range(2*i - 1):
        print('*', end='')
    print()
for i in range(a - 1, 0, -1):
    for j in range(a - i):
        print(' ', end='')
    for j in range(2*i - 1):
        print('*', end='')
    print()