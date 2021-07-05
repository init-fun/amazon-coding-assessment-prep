# def getMax(cut_arr):
#     index = 1
#     max_h = cut_arr[0]
#     while index < len(cut_arr):
#         max_h = max(abs(cut_arr[index - 1] - cut_arr[index]), max_h)
#         index += 1
#     return max_h


def getMax(cuts):
    max_diff = cuts[0]
    for i in range(1, len(cuts)):
        max_diff = max(abs(cuts[i] - cuts[i - 1]), max_diff)
    return max_diff


def cake(h, w, hc, vc):
    hc.sort()
    vc.sort()

    hc += [h]
    vc += [w]
    max_height = getMax(hc)
    max_width = getMax(vc)
    print(max_width, max_height)
    return max_height * max_width


h = 5
w = 4
hc = [1, 2, 4]
vc = [1, 3]

# h = 5
# w = 4
# hc = [3, 1]
# vc = [1]
print(cake(h, w, hc, vc))
