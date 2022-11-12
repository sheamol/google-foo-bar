def solution(x, y):
    m, f = (max(int(x),int(y))), (min(int(x),int(y)))
    counter = 0
    while f > 0:
        counter += m // f   # How many divisions it'll take to get to target
        m, f = f, m % f     # Find remainder and repeat
    if m !=1:               # Check remainder is equal to 1, if not, them impossible
        return "impossible"
    return str(counter-1)


print(solution(7, 4))
