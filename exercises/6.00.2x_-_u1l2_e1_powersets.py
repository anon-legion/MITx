# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 09:17:54 2021

@author: =GV=
"""
# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test jth bit of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo

def powerSet2(items):
    N = len(items)
    # enumerate the 3**N possible combinations
    for i in range(3**N):
        # print(i)
        bag1 = []
        bag2 = []
        for j in range(N):
            # test jth bit of integer i
            if (i // 3**j) % 3 == 1 :
                bag1.append(items[j])
            elif (i // 3**j) % 3 == 2:
                bag2.append(items[j])
        yield (bag1, bag2)
        

items = ['apple', 'banana']
test1 = powerSet(items)
test2 = powerSet2(items)

for i in range(2**len(items)):
    print(next(test1))

for i in range(3**len(items)):
    print(next(test2))
    
    
