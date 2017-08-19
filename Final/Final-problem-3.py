# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 20:11:32 2017

@author: Erick
"""

def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    num = []
    answer = 0
    for c in s:
        try:
            num.append(int(c))
        except ValueError:
            pass
    if len(num) == 0:
        raise ValueError
    for i in num:
        answer += i
    return(answer)


test = 'a;35d4'
print(sum_digits(test))