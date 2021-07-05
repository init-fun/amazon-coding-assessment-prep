from math import dist, pi, sqrt
from heapq import *


def getDistance(tup):
    x = tup[0]
    y = tup[1]
    return -sqrt(x ** 2 + y ** 2)


def closeToOrigin(points, k):
    # arr = []
    # distance_heap = []

    # for i in points:
    #     heappush(arr, getDistance(i))
    #     heappush(distance_heap, i)

    #     if len(arr) > k:
    #         heappop(arr)
    #         heappop(distance_heap)
    maxheap = []
    for i in range(k):
        heappush(maxheap, points[i])

    for i in range(k, len(points)):
        heappush(maxheap, points[i])
        cd = getDistance(points[i])
        hd = getDistance(heappop(maxheap))
        if cd < hd:
            heappop(maxheap)

    return list(maxheap)


point = [(1, 3), (3, 4), (2, -1)]
K = 2
print(closeToOrigin(point, K))