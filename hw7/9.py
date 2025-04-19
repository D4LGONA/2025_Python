def isrev(n):
    if n == int(str(n)[::-1]):
        return True
    return False

def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = eval(input())
res = 0

while True:
    if isrev(n) and isPrime(n):
        res = n
        break
    else:
        n += 1
print(res)