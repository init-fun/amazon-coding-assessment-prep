from heapq import *


def rearrnage(s):
    tmp_dict = {}
    for i in s:
        if i not in tmp_dict:
            tmp_dict[i] = 1
        else:
            tmp_dict[i] += 1

    maxHeap = []
    for c, f in tmp_dict.items():
        heappush(maxHeap, (-f, c))

    prev_char = None
    prev_freq = 0
    res = ""
    while maxHeap:
        if prev_char and -prev_freq > 0:
            heappush(maxHeap, (prev_freq, prev_char))
        prev_freq, prev_char = heappop(maxHeap)
        prev_freq += 1
        res += prev_char
        prev_char = prev_char
    return res


s = "Programming"
print(rearrnage(s))