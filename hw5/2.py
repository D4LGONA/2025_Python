import random

a, b = random.randint(1, 6), random.randint(1, 6)
c, d = random.randint(1, 6), random.randint(1, 6)
print("A의 주사위 숫자는 %d %d입니다." % (a, b))
print("B의 주사위 숫자는 %d %d입니다." % (c, d))
if a+b > c+d:
    print("A가 이겼네요.")
elif a+b < c+d:
    print("B가 이겼네요.")
else:
    print("둘이 비겼네요.")