import random

count = 0
straight = 0

if __name__ == "__main__":
    while True:
        count += 1
        numbers = [random.randint(1, 6) for _ in range(6)]
        if len(set(numbers)) == 6:
            straight += 1
        if len(set(numbers)) == 1:
            break

    print("6개 주사위가 모두 동일한 숫자가 나옴-->" , *numbers)
    print("6개가 동일한 숫자가 나올 때까지 주사위를 던진 횟수-->", count)
    print("6개가 동일한 숫자가 나올 때까지, 1~6의 연속번호가 나온 횟수-->",straight)