def xor(n):
    val = n % 4
    if val == 0:
        return n
    if val == 1:
        return 1
    if val == 2:
        return n + 1
    return 0


def solution(start, length):
    if length == 1:
        return start

    res = xor(start + 2*(length-1))

    if start > 1:
        res = res ^ (start - 1)

    for i in range(length-2):
        res = res ^ (start + length*(2 + i) - 1 + length - 2 - i) ^ (start + length*(2 + i) - 1)
    return res


print(solution(0, 3))
