sum = 0.0
count = 0.0

for _ in range(20):
    tmp = input().split()
    if tmp[2] == 'P': continue
    grade = 0.0
    if tmp[2] == 'A+' : grade = 4.5
    elif tmp[2] == 'A0': grade = 4.0
    elif tmp[2] == 'B+': grade = 3.5
    elif tmp[2] == 'B0': grade = 3.0
    elif tmp[2] == 'C+': grade = 2.5
    elif tmp[2] == 'C0': grade = 2.0
    elif tmp[2] == 'D+': grade = 1.5
    elif tmp[2] == 'D0': grade = 1.0
    sum += float(tmp[1]) * grade
    count += float(tmp[1])

print("%.6f" % (sum / count))
