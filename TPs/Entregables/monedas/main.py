import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

def fun1(coins, value):
    if value == 0:
        return 0

    if coins[0] > value:
        return 10000000

    min = 10000000
    for index in range(len(coins)):
        if (coins[index] > value):
            break

        temp = fun1(coins, value - coins[index])
        min = min if min < temp else temp
    
    return 1 + min

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

coins = [3,5]
for i in range(1,10):

    #start_time = time.perf_counter()
    #res = fun2(n,k)
    #print( "items: ", i, "result: ", res, "time: ", time.perf_counter() - start_time)

    start_time = time.perf_counter()
    res = fun1(coins, i)
    print( "coins: ", coins, "result: ", res, "time: ", time.perf_counter() - start_time)
    print();
    print();
