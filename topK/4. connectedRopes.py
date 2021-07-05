from heapq import *


def connectedRopes(arr):
    minheap = []
    min_sum = 0
    for i in arr:
        heappush(minheap, i)
    while len(minheap) != 1:
        fele = heappop(minheap)
        sele = heappop(minheap)
        min_sum += fele + sele
        heappush(minheap, fele + sele)
    return min_sum


print(connectedRopes([3, 4, 5, 6]))