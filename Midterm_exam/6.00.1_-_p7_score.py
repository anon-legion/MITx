# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 21:26:41 2020

@author: Anon
"""

def score(word, f):
    """
       word, a string of length > 1 of alphabetical 
             characters (upper and lowercase)
       f, a function that takes in two int arguments and returns an int

       Returns the score of word as defined by the method:

    1) Score for each letter is its location in the alphabet (a=1 ... z=26) 
       times its distance from start of word.  
       Ex. the scores for the letters in 'adD' are 1*0, 4*1, and 4*2.
    2) The score for a word is the result of applying f to the
       scores of the word's two highest scoring letters. 
       The first parameter to f is the highest letter score, 
       and the second parameter is the second highest letter score.
       Ex. If f returns the sum of its arguments, then the 
           score for 'adD' is 12 
    """
    import string
    scores = []
    for x in range(len(word)):
        scores.append((string.ascii_lowercase.find(word[x].lower()) + 1) * x)
    a, b = sorted(scores)[-2: ]
    return f(b, a)
    

def top2(x=0, y=0):
    return x + y


# #test
# word = 'asdjkhjkq'
#function = top2

# print(score('adD', top2))

