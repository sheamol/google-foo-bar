import numpy as np

def solution(n):
    if n < 3:
        return 0

    m = np.zeros((n+1, n+1))    # initalise array to keep track of no. stairs for each no. bricks
    m[0][0] = 1                 # set the case for n = 3 to 1

    for i in range(n):
        for ii in range(n + 1):
            m[i + 1][ii] = m[i][ii]
            if ii > i:
                m[i + 1][ii] += m[i][ii - i - 1]        # Difference equation to find number of solutions for next n
    return int(m[n][n] -1)

print(solution(200))
