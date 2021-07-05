from heapq import *
import heapq


def find_top_k_elements(arr, k):
    myheap = []
    for i in arr:
        heappush(myheap, i)
        if len(myheap) > k:
            heappop(myheap)
    return list(myheap)


# arr = [3, 1, 5, 12, 2, 11]
k = 3
arr = [5, 12, 11, -1, 12]

print(find_top_k_elements(arr, k))