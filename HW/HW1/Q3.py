# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 20:19:35 2018

@author: Yijie
"""

#Q3
#range(start, stop, step), default step is 1.
#loop until value is stop-1

# iteration
def sum_it(n):
    sum_it = 0
    for i in range(1,n+1):
        sum_it +=i
    return sum_it
print(sum_it(100))

# recursion
# assign number using '=', for making a judgement using '=='
def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)
print(sum(100))