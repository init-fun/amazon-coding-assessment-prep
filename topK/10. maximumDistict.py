from heapq import *


def maximumDistinct(arr, k):
    if len(arr) < k:
        return arr
    distict_count = 0

    tmp_dict = {}
    for i in arr:
        if i not in tmp_dict:
            tmp_dict[i] = 1
        else:
            tmp_dict[i] += 1

    minHeap = []
    for chr, freq in tmp_dict.items():
        if freq == 1:
            distict_count += 1
        else:
            heappush(minHeap, (freq, chr))

    # 2:4, 3:5, 4:3


arr = [1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5]
k = 2
print(maximumDistinct(arr, k))