from decimal import Decimal, localcontext
import math


def _solution(s):
    a = Decimal(s)
    with localcontext() as ctx:
        ctx.prec = 102
        r = Decimal(2).sqrt()
        s = r / (r - 1)

        def solve(k):
            if k == 0:
                return 0
            n = int(r * k)
            n_prime = int(Decimal(n) / s)
            return (n * (n + 1)) / 2 - solve(n_prime) - n_prime * (n_prime + 1)

        return str(int(solve(a)))


def solution(s):
    a = Decimal(s)
    with localcontext() as ctx:
        ctx.prec = 102

        def solve(n):
            n = Decimal(n)
            if n == 0:
                return 0
            n_prime = Decimal(math.floor((Decimal(2).sqrt() - Decimal(1)) * Decimal(n)))

            return n * n_prime + n * (n + Decimal(1))/2 - n_prime * (n_prime + Decimal(1))/Decimal(2) - solve(n_prime)

        return str(int(solve(a)))


print(solution("77"))
print(solution("5"))
print(solution(str(10e100)))
print(_solution(str(10e100)))
