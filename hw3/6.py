s = input("글자 입력 : ")

if s >= '0' and s <= '1':
    print("2진수 또는 8진수 또는 10진수 또는 16진수 입니다.")
elif s <= '7':
    print("8진수 또는 10진수 또는 16진수 입니다.")
elif s <= "9":
    print("10진수 또는 16진수 입니다.")
elif "A" <= s <= "F" or 'a' <= s <= 'f':
    print("16진수 입니다.")
else:
    print("숫자가 아닙니다.")
