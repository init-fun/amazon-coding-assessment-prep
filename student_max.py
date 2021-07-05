# import heapq


# def maxAverageRatio(classes, e):
# heap = []
# for i, j in classes:
#     diff = (i + 1) / (j + 1) - (i / j)
#     heapq.heappush(heap, (-diff, i, j))
# while e > 0:
#     diff, i, j = heapq.heappop(heap)
#     i += 1
#     j += 1
#     diff = (i + 1) / (j + 1) - (i / j)
#     heapq.heappush(heap, (-diff, i, j))
#     e -= 1
# ans = 0
# for diff, i, j in heap:
#     ans += i / j
# return ans / len(classes)

from heapq import *


def maxAverageRatio(classes, extra):
    maxHeap = []
    for i, j in classes:
        diff = ((i + 1) / (j + 1)) - (i / j)
        heappush(maxHeap, (-diff, i, j))

    print(maxHeap)

    while extra > 0:
        diff, i, j = heappop(maxHeap)
        i += 1
        j += 1
        diff = ((i + 1) / (j + 1)) - (i / j)
        heappush(maxHeap, (-diff, i, j))
        extra -= 1

    print(maxHeap)
    ans = 0
    for diff, i, j in maxHeap:
        ans += i / j
    return ans / len(classes)


classes = [[1, 2], [3, 5], [2, 2]]
extraStudents = 2
print(maxAverageRatio(classes, extraStudents))