M = eval(input())
N = eval(input())
L = [True] * (N+1)

L[0] = L[1] = False
for i in range(2, int(N ** 0.5) + 1):
    if L[i] == True:
        for j in range( 2, N):
            if i * j <= N:
                L[i*j] = False
            else:
                break

total = 0
small = 0
for i in range(M, N+1):
    if L[i] == True:
        total += i
        if small == 0:
            small = i

if total == 0:
    print(-1)
else:
    print(total)
    print(small)