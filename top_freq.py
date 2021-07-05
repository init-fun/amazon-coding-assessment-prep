from heapq import *


def top_freq(arr, k):
    tmp_dict = {}
    for i in arr:
        if i not in tmp_dict:
            tmp_dict[i] = 1
        else:
            tmp_dict[i] += 1

    maxHeap = []
    for c, freq in tmp_dict.items():
        if len(maxHeap) > k:
            heappop(maxHeap)
        else:
            heappush(maxHeap, (freq, c))

    return [i[1] for i in maxHeap]


arr = ["i", "love", "i", "love", "coding", "leetcode"]
k = 2
print(top_freq(arr, k))
