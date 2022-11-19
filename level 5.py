"""Solution to find a sum of Beatty Sequence with alpha of sqrt 2."""
from decimal import Decimal, getcontext

# Set decimal precision globally and declare global constants needed for a Beatty sequence
getcontext().prec = 102
R = Decimal(2).sqrt()
S = Decimal(2) + Decimal(2).sqrt()  # s = r/(r-1) which in this case is 2 + sqrt(2)


def _solve(k):
    """Recursive function to find summation using Raleigh-Beatty Theorem."""
    if k == 0:
        return 0
    n = int(R * k)
    n_prime = int(Decimal(n) / S)
    return n * (n + 1) / 2 - n_prime * (n_prime + 1) - _solve(n_prime)


def solution(s):
    """Take position of stopping position for the summation, convert to decimal, then returnS summation as string."""
    a = Decimal(s)
    return str(_solve(a))


print(solution("77"))
print(solution("5"))
print(solution(str(10e100)))
