# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 21:10:55 2021

@author: jrbrad
"""

import time

''' This wrapper function creates a timer for function execution '''
def time_fn(fn):
    def inner_f(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        print(f'Execution time for function {fn.__name__}() if {time.time() - start} seconds')
        return result
    return inner_f

@time_fn
def loop(n):
    result = 0
    for i in range(n):
        result += i
    return result

print(loop(50000))