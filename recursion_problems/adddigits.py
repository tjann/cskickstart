def addDigits(num):
    if num // 10 < 1:
        return num
    else:
        s = 0
        while num > 0:
            s += num % 10
            num //= 10
    return addDigits(s)
print(addDigits(23))
print(addDigits(554))
