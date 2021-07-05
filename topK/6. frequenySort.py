from heapq import *


def freqSort(s):
    tmp_dict = {}
    for i in s:
        if i not in tmp_dict:
            tmp_dict[i] = 1
        else:
            tmp_dict[i] += 1

    maxheap = []
    for ele, freq in tmp_dict.items():
        heappush(maxheap, (-1 * freq, ele))

    sorted_string = []
    res = ""
    for i in range(len(maxheap)):
        f, e = heappop(maxheap)
        res += str(e) * (-1 * f)

    return res


s = "Programming"
print(freqSort(s))