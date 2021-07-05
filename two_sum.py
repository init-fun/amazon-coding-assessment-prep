def twosum(arr, target):
    ans = set()
    traversal_set = set()
    for num in arr:
        diff = target - num
        if diff in traversal_set:
            tup = (num, diff) if num > diff else (diff, num)
            if tup not in ans:
                ans.add(tup)
        traversal_set.add(num)
    return len(ans)


arr = [1, 1, 2, 45, 46, 46]
k = 47
# arr = [1, 5, 5, 1]
# k = 6
arr = [5, 5, 5]
k = 10

print(twosum(arr, k))