n = int(input('연도를 입력하세요: '))
if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
    print("%d년은 윤년입니다." % n)
else:
    print("%d년은 윤년이 아닙니다." % n)