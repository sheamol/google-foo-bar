import itertools


def solution(time, time_limit):
    """For a given time matrix, find max number of nodes to visit
    Uses a brute force method, permuting through all the available bunnies, taking one less each time
    until time constraint is met"""

    rows = len(time)
    bunnies = rows - 2

    # deal with negative times i.e. increase in timer amount
    for i in range(rows):
        for ii in range(rows):
            for iii in range(rows):
                time[ii][iii] = min(time[ii][iii], time[ii][i] + time[i][iii])

    # if any diagonals are < 0 then you can create a path going to yourself thus giving infinite time,
    # thus all bunnies saved
    for r in range(rows):
        if time[r][r] < 0:
            return range(bunnies)

    # permute through all possible bunny paths, starting at 0 ending at -1 (the end)
    for i in reversed(range(bunnies + 1)):  # reverse used to start with all bunnies and work backwards
        for perm in itertools.permutations(range(1, bunnies + 1), i):
            total_time = 0
            path = [0] + list(perm) + [-1]  # create path for bunny collection, start at 0, end at -1
            for step in range(len(path) - 1):
                total_time += time[path[step]][path[step + 1]]  # get time taken to get from current to next from
                # matrix

            if total_time <= time_limit:
                return sorted(list(i - 1 for i in perm))    # -1 needed as bunny 0 is in row 1
    return None


print(solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1))
print(solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3))
