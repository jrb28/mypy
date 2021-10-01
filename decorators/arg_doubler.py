# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 20:46:55 2021

@author: jrbrad
"""

from functools import wraps

''' Wrapper function that doubles the numerical arguments '''
''' Positional and named arguments are received in general form with *args and **kwargs '''
''' Using @wraps(fn) causes the wrapped function to inherit properties of the passed function '''

def doubler(fn):
    @wraps(fn)
    def inner_f(*args, **kwargs):
        print(f'The numerical arguments {fn.__name__} function are being doubled.')
        
        
        ''' Loop through and double int and float values '''
        args = list(args) # args come in an (immutable) tuple
        for i in range(len(args)):
            if isinstance(args[i], int) or isinstance(args[i], float):
                args[i] = 2 * args[i]
            
        for k,v in kwargs.items():
            if isinstance(kwargs[k], int) or isinstance(kwargs[k], float):
                kwargs[k] = 2 * kwargs[k]
        
        return fn(*args, **kwargs)
    
    return inner_f

@doubler
def mult2(x):
    return(2*x)

@doubler
def dict2(**x):
    return(x)
    

print(mult2(2))
print(mult2.__name__, '\n')

my_dict = {'k':3, 'm':'x', 'n':4.5}
result = dict2(**my_dict)
for k,v in result.items():
    print(k,v)
print(dict2.__name__)