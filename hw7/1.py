import random
nn = []
for _ in range(10) :
    num = random.randrange(1, 100)
    nn.append(num)
hap = 0
for i in range(10) :
    num = nn[i]
    hap += num
print(hap)
