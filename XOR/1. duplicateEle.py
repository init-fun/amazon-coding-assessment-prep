def duplicateEle(arr):
    arr_len = max(arr)
    res = 0
    for i in range(arr_len + 1):
        res ^= i
    for i in arr:
        res ^= i

    return res


arr = [1, 5, 2, 6, 4]
print(duplicateEle(arr))