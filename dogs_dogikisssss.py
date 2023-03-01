def max_zeros(numb: str):

    max_num0 = 0
    num0 = 0

    for i in numb:

        if i == '0':
            num0 += 1
        else:
            max_num0 = max(max_num0, num0)
            num0 = 0

    if max_num0 == 0 and num0 > 0:
        return num0

    return max_num0

result = max_zeros("10001011010000011010")
assert result == 5
result = max_zeros("000000000000000000")
assert result == 18
result = max_zeros("1111111111111111111")
assert result == 0
result = max_zeros("2202020202020200000002")
assert  result == 7
result = max_zeros("")
assert result == 0