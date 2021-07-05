from heapq import *


def kthSmallest(arr, k):
    max_heap = []
    i = 0
    arr_len = len(arr)
    while i < arr_len:
        heappush(max_heap, -1 * arr[i])
        i += 1

    for index in range(i):
        heappush(max_heap, -1 * arr[index])
        if len(max_heap) > k:
            heappop(max_heap)

    return -1 * heappop(max_heap)


# arr = [1, 5, 12, 2, 11, 5]
# k = 4
arr = [5, 12, 11, -1, 12]
K = 3
print(kthSmallest(arr, K))
