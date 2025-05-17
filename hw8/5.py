data = [("토마스", 5), ("헨리", 8), ('에드워드', 9), ('에밀리', 5),
        ('토마스', 4), ('헨리', 7), ('토마스', 3), ('에밀리', 8), ('퍼시', 5),
        ('고든', 13)]

print("기차 수송량 목록 =>", data)
print("-" * 40)

cargo_sum = {}
for key, value in data:
    cargo_sum[key] = cargo_sum.get(key, 0) + value

sorted_cargo = sorted(cargo_sum.items(), key=lambda x: x[1], reverse=True)

# 3. 출력
print("기차       총수송량   순위")
print("-" * 40)

prev_amount = None
rank = 0
skip = 1

for i, (name, total) in enumerate(sorted_cargo):
    if total != prev_amount:
        rank += skip
        skip = 1
    else:
        skip += 1
    print(f"{name:<10}{total:<10}{rank}")
    prev_amount = total
