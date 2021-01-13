# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 21:26:41 2020

@author: Anon
"""

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    keys = []
    for x in aDict:
        if aDict[x] == target:
            keys.append(x)
        else:
            continue
    return sorted(keys)