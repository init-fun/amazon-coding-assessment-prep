def duplicateEle(arr):
    res = 0
    for i in arr:
        res ^= i

    # get the rightmost bit that is '1'
    rightmost_bit = 1
    while rightmost_bit & res == 0:
        rightmost_bit = rightmost_bit << 1
    num1, num2 = 0, 0
    for num in arr:
        if num & rightmost_bit != 0:
            num1 ^= num
        else:
            num2 ^= num

    return num1, num2


arr = [1, 4, 2, 1, 3, 5, 6, 2, 3, 5]
print(duplicateEle(arr))