# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 11:24:20 2020

@author: Anon
"""

"""
input:
    L: assumes a list of integers
output:
    given the appropriate inputs the function returns the length of the longest run of monotonically increasing numbers occurring in L
    where a number at index i+1 in the sequence is either greater than or equial to the number at index i.
NOTE:   both functions are different solutions to the same problem
"""

def longestRun(L): # less lines of code but is technically polynomial time complexity O(n^2)
    recent_index = 0
    longest = [1]
    for i in range(len(L)):
        if i == recent_index:
            for j in range(i + 1, len(L) + 1):
                if j == len(L) or L[j] < L[j - 1]:
                    recent_index = j
                    longest.append(len(L[i:j]))
                    break
    return max(longest)

def longestRun2(L): # more lines of code but is linear time complexity O(n) 
    run = False
    longest = [1]
    for i in range(1, len(L)):
        if L[i] >= L[i - 1] and i == len(L) - 1:
            if not run:
                start = i - 1
            longest.append(len(L[start:]))
        elif L[i] >= L[i - 1] and not run:
            run = True
            start = i - 1
        elif L[i] < L[i - 1] and run:
            run = False
            longest.append(len(L[start:i]))
        else:
            continue
    return max(longest)


# test
test = [1, 0, 0, 0, 4, 5, 1, 2, 9, 4, -1, 0]
print('longestRun =\t', longestRun(test))
print('longestRun2 =\t', longestRun2(test))
