import itertools


def convert_to_path(perm):
    perm = list(perm)
    perm = [0] + perm + [-1]
    path = list()
    for i in range(1, len(perm)):
        path.append((perm[i - 1], perm[i]))
    return path


def solution(time, time_limit):
    rows = len(time)
    bunnies = rows - 2

    print('\n'.join(map(str, time)))
    print('')

    for i in range(rows):
        for ii in range(rows):
            for iii in range(rows):
                time[ii][iii] = min(time[ii][iii], time[ii][i] + time[i][iii])

    print('\n'.join(map(str, time)))
    print('')

    for r in range(rows):
        if time[r][r] < 0:
            return [i for i in range(bunnies)]

    for i in reversed(range(bunnies + 1)):
        for perm in itertools.permutations(range(1, bunnies + 1), i):
            total_time = 0
            path = convert_to_path(perm)
            for start, end in path:
                total_time += time[start][end]
            if total_time <= time_limit:
                return sorted(list(i - 1 for i in perm))
    return None


print(solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1))
# print(solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3))
