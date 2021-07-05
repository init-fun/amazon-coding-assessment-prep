from heapq import *


def sumOfElements(arr, p, q):
    maxHeap = []
    for i in arr:
        heappush(maxHeap, i)
    i = 1
    len_heap = len(maxHeap)
    total = 0

    while i <= len_heap:
        if i > p and i < q:
            total += heappop(maxHeap)
        else:
            heappop(maxHeap)
        i += 1
    return total


arr = [1, 3, 12, 5, 15, 11]
K1 = 3
K2 = 6
print(sumOfElements(arr, K1, K2))
