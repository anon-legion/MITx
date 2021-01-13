# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 21:26:41 2020

@author: Anon
"""

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    ans = 0
    for x in range(len(listA)):
        ans += (listA[x] * listB[x])
    return ans