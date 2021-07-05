def duplicateEle(arr):
    res = 0
    for i in arr:
        res ^= i
    return res


arr = [1, 4, 2, 1, 3, 2, 3]
print(duplicateEle(arr))