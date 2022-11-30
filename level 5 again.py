from math import factorial
from collections import Counter
from fractions import gcd


def cycle_counter(cycle, block):
    cycle_count = factorial(block)
    for a, b in Counter(cycle).items():
        cycle_count //= (a ** b) * factorial(b)
    return cycle_count        


def gird_maker(block, i = 1):
    yield [block]
    for i in range(i, block//2 + 1):
        for ii in gird_maker(block - i, i):
            yield [i] + ii


def solution(w, h, s):    
    grid_count = 0
    for cycle_w in gird_maker(w):
        for cycle_h in gird_maker(h):            
            cycle_count = cycle_counter(cycle_w, w) * cycle_counter(cycle_h, h)
            grid_count += cycle_count * (s ** sum([sum([gcd(i, ii) for i in cycle_w]) for ii in cycle_h]))
              
    return str(grid_count // (factorial(w) * factorial(h)))

print(solution(2, 3, 4))
print(solution(2, 2, 2))
