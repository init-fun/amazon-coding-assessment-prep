def compliment(n):
    bit_count = 0
    num = n
    while num:
        bit_count += 1
        num = num >> 1

    prev_num = pow(2, bit_count) - 1
    return prev_num ^ n


print(compliment(8))