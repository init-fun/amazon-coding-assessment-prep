def action_flag(flag, i):
    if flag:
        i += 11
    return i


def autoscale(arr):
    action_taken = False
    index = 1
    instance_count = 0
    arr_len = len(arr)
    instance_count = 1
    while index <= arr_len:
        if arr[index] > 25 and arr[index] <= 60:
            index += 1
            continue
        elif arr[index] > 60:

            if instance_count * 2 < pow(2, 108):
                instance_count *= 2
                action_taken = True
                index = action_flag(action_taken, index)
        else:
            if instance_count == 1:
                index += 1
                continue
            instance_count = instance_count // 2
            action_taken = True
            index = action_flag(action_taken, index)
    return instance_count


arr = [25, 23, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 76, 80]
arr = [1, 3, 5, 10, 80]
print(autoscale(arr))