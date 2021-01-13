# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 11:39:51 2020

@author: Anon
"""

def f(a,b):
    return a + b

def dict_interdiff(d1, d2):
    """
    input:
        d1, d2: dicts whose keys and values are integers
    output:
        given the appropriate inputs the function returns a tuple of two dictionaries: a dictionary of the intersect of d1 and d2
        and a dictionary of the difference of d1 and d2
    NOTE:   the value of intersecting keys are applied to a function f() where the value of the common key in d1 is the first parameter
            and the value of the common key in d2 is the second parameter respectively
    """
    intersect = {key:f(d1[key],d2[key]) for key in d1 if key in d2}
    difference = {key:d1[key] for key in d1 if key not in d2}
    for key in d2:
        if key not in d1:
           difference[key] = d2[key] 
    return (intersect, difference)


# # test
# d1 = {1:30, 2:20, 3:30, 5:80}
# d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
# print(dict_interdiff(d1, d2))