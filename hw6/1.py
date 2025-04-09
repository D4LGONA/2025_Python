sum = 0

for i in range(3333, 10000):
    if i % 1234 == 0: continue
    sum += i
    if sum >= 100000:
        sum -= i
        break
print(sum)