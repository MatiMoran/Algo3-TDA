import sys
import time

sys.setrecursionlimit(100_000_000)

memoria = [-1 for _ in range(10_000_001)]
MOD = 10 ** 9 + 7


def f(n):
    if n == 0:
        return 1
    if n == 1:
        return 3
    if memoria[n] == -1:
        memoria[n] = f(n-1)+2*f(n-2) % MOD
    return memoria[n]

def f2(n):
    if n == 0:
        return 1
    if n == 1:
        return 3
    if n == 2:
        return 5
    if n not in memoria2:
        k = n // 2
        if n % 2 == 1:
            memoria2[n] = f2(k) ** 2 + 2 * f2(k - 1) ** 2
            memoria2[n] %= MOD
        else:
            memoria2[n] = f2(k) * f2(k - 1) + 2 * f2(k - 1) * f2(k - 2)
            memoria2[n] %= MOD
    return memoria2[n]


if __name__ == '__main__':
    for _n in [0, 1, 2, 3, 4, 5, 10, 100, 1000,  10_000, 100_000, 1_000_000, 10_000_000]:
        memoria2 = {}
        memoria = [-1 for _ in range(_n+1)]
        t = time.time()
        res = f2(_n)
        dt = time.time() - t
        print(f"f({_n}) = {res}, time = {dt}")
