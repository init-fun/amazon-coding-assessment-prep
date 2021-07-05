from collections import Counter
from heapq import *


def kFrequent(arr, k):
    tmp_dict = {}
    i = 0
    start = 0
    len_arr = len(arr)
    while i < len_arr:
        if arr[i] not in tmp_dict:
            tmp_dict[arr[i]] = 0
        tmp_dict[arr[i]] += 1
        i += 1
        while len(tmp_dict) > k:
            char_to_remove = arr[start]
            tmp_dict[char_to_remove] -= 1
            if tmp_dict[char_to_remove] == 0:
                del tmp_dict[char_to_remove]
            start += 1
    return list(tmp_dict.keys())


arr = [1, 3, 1, 5, 12, 11, 12, 11]
K = 2
arr = [5, 12, 11, 3, 11]
print(kFrequent(arr, K))