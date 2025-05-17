def base2(n):
    if n < 2:
        return str(n)
    return base2(n // 2) + str(n % 2)

def base8(n):
    if n < 8:
        return str(n)
    return base8(n // 8) + str(n % 8)

def base16(n):
    hex_chars = "0123456789ABCDEF"
    if n < 16:
        return hex_chars[n]
    return base16(n // 16) + hex_chars[n % 16]

num = int(input("10진수 입력 --> "))
print("2진수  :", base2(num))
print("8진수  :", base8(num))
print("16진수 :", base16(num))
