def mirrored(n):
    return str(n) == str(n)[::-1]

def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


a = eval(input())
count = 0
num = 2
while True:
    if mirrored(num) and isPrime(num):
        count += 1
    if count == a: break
    num += 1

print(num)
