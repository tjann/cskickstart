def addDigits(num):
    if num  < 10:
        return num
    else:
        return addDigits(addDigits(num//10) + addDigits(num % 10))
print(addDigits(23))
print(addDigits(554))
