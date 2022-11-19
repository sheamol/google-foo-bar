def solution(x, y):
    first = x
    second = y
    if len(x) > len(y):
        second = x
        first = y

    for item in first:
        second.remove(item)
    return second


print(solution([13, 5, 6, 2, 5], [5, 2, 5, 13]))
print(solution([14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50]))
