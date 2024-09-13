import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

def fun1(items_values, items_weights, n_items, max_weight):
    if n_items == 0:
        return 0
    if max_weight == 0:
        return 0
    if items_weights[n_items-1] > max_weight:
        return fun1(items_values, items_weights, n_items-1, max_weight)

    aux1 = fun1(items_values, items_weights, n_items-1, max_weight)
    aux2 = items_values[n_items-1] + fun1(items_values, items_weights, n_items-1, max_weight - items_weights[n_items-1])
    return aux1 if aux1 > aux2 else aux2

def fun2_internal(items_values, items_weights, n_items, max_weight, cache):
    if (cache[n_items, max_weight] != -1):
        return cache[n_items, max_weight]
    if n_items == 0:
        return 0
    if max_weight == 0:
        return 0
    if items_weights[n_items-1] > max_weight:
        return fun2_internal(items_values, items_weights, n_items-1, max_weight, cache)

    aux1 = fun2_internal(items_values, items_weights, n_items-1, max_weight, cache)
    aux2 = items_values[n_items-1] + fun2_internal(items_values, items_weights, n_items-1, max_weight - items_weights[n_items-1], cache)
    return aux1 if aux1 > aux2 else aux2

def fun2(items_values, items_weights, n_items, max_weight):
    cache = np.full((n_items + 1, max_weight + 1), -1)

    for i in range(0, n_items + 1):
        for j in range(0, max_weight + 1):
            cache[i,j] = fun2_internal(items_values, items_weights, i, j, cache)

    return cache[n_items, max_weight]

profit = [60, 100, 120] 
weight = [10, 20, 30] 
W = 50
n = len(profit) 
print(fun2(profit, weight, n, W))
print(fun1(profit, weight, n, W))

max_weight = 200

for i in [1,5,10,15,20]:
    n_items = i
    items_values = np.round(np.random.rand(n_items,1) * 100).astype(int)
    items_weights = np.round(np.random.rand(n_items,1) * 10).astype(int)

    start_time = time.perf_counter()
    res = fun2(items_values, items_weights, n_items, max_weight)
    print( "items: ", i, "result: ", res, "time: ", time.perf_counter() - start_time)

    start_time = time.perf_counter()
    res = fun1(items_values, items_weights, n_items, max_weight)
    print( "items: ", i, "result: ", res, "time: ", time.perf_counter() - start_time)
    print();
    print();
