import random

numbers = [random.randint(1, 20) for _ in range(20)]
print("생성된 리스트", numbers)
s_numbers = set(numbers)
for n in s_numbers:
    print("숫자 %d는(은) 뽑혔습니다." %n)