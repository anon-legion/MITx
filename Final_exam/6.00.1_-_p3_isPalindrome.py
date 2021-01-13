# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 11:09:50 2020

@author: Anon
"""

def isPalindrome(aString): # iterative solution
    '''
    aString: a string
    '''
    temp = ''
    for i in range(len(aString) - 1, -1, -1):
        temp += aString[i]
    return temp.lower() == aString.lower()

def isPalindrome2(aString): # recursive solution
    '''
    aString: a string
    '''
    temp_word = aString.lower()
    def recurPalindrome(aString):
        if len(aString) <= 1:
            return True
        else:
            return aString[0] == aString[-1] and recurPalindrome(aString[1:-1])
    return recurPalindrome(temp_word)