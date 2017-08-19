# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 17:05:46 2017

@author: Erick
"""

def max_val(t, high = 0):
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """
    for x in t:
        if type(x) == tuple:
            for i in range(len(x)):
                if x[i] > high:
                    high = x[i]
        elif type(x) == list:
            return max_val(x, high)
        elif x > high:
            high = x
    return(high)
