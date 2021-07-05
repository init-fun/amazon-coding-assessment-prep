def primechecker(num):
    if num > 1:
        for i in range(2, 1 + (num // 2)):
            if num % i == 0:
                return False
        else:
            return True
    return False


print(primechecker(3117))
print(primechecker(117))