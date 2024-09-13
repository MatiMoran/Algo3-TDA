import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

def fun1(n,k):
    if k == 0 or k == n:
        return 1

    return fun1(n-1,k-1) + fun1(n-1,k)

def fun2_internal(n,k, cache):
    if (cache[n, k] != -1):
        return cache[n, k]
    if k == 0 or k == n:
        return 1
    if k > n:
        return -1
    return fun2_internal(n-1,k-1,cache) + fun2_internal(n-1,k,cache)

def fun2(n,k):
    cache = np.full((n+1,k+1), -1)

    for i in range(0, n + 1):
        for j in range(0, k + 1):
            cache[i,j] = fun2_internal(i,j,cache)

    return cache[n, k]

for i in [5,10,15,20]:
    n = 2*i
    k = i

    start_time = time.perf_counter()
    res = fun2(n,k)
    print( "items: ", i, "result: ", res, "time: ", time.perf_counter() - start_time)

    start_time = time.perf_counter()
    res = fun1(n,k)
    print( "items: ", i, "result: ", res, "time: ", time.perf_counter() - start_time)
    print();
    print();
