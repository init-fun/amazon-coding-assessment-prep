def splitNum(s):
    """Split a string into all possible combinations"""
    assert "," not in s
    splits = []
    i = 0
    while i < 2 ** (len(s) - 1):
        b = str(bin(i))[2:]
        b = "0" * (len(s) - len(b) - 1) + b + "0"
        p = 0
        r = ""

        while p < len(s):
            r += s[p]
            if b[p] == "1":
                r += ","
            p += 1
        nums = [int(x) for x in r.split(",")]
        splits.append(nums)
        i += 1
    return splits


def isPrime(n):
    """A really simplistic way of identifying a prime number"""
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def areAllPrimes(s):
    """Return True if all numbers in the set are Prime numbers"""
    for num in s:
        if not isPrime(num):
            return False
    return True


s = "31173"
for splits in splitNum(s):
    if areAllPrimes(splits):
        print(splits)

print(splitNum(s))