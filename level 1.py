def solution(x, y):
    if len(x) > len(y):
        x, y = y, x

    for item in x:
        y.remove(item)
    return y

def _solution(x, y):
    return list(set(x).symmetric_difference(set(y)))


print(_solution([13, 5, 6, 2, 5], [5, 2, 5, 13]))
print(_solution([14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50]))
