'''
Created on February 12, 2016
@author:   Jordan Handwerger
Pledge:    I pledge my honor that I have abided by the Stevens Honor System -JH

CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.
from test.profilee import helper

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# your code goes here

def giveChange(target, numberList):
    '''Returns a list containing the lowest number of values in numberList that sum
     to the target, and a list of those values.'''  
    if target == 0:
        return [0, [] ]
    elif numberList == []:
        return [ float("inf"), [] ]
    elif numberList[0] > target:
        return giveChange(target, numberList[1:])
    useIt = giveChange(target-numberList[0], numberList)
    useIt = [useIt[0] + 1, useIt[1] + [ numberList[0] ] ]
    loseIt = giveChange(target, numberList[1:])
    if useIt[0] < loseIt[0]:
        return useIt
    return loseIt

# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordsWithScore(dct, scores):
    '''Returns a List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(scrabbleScores, Dictionary) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    return combine(dct, list(map(helper(scores), dct) ))

    
def helper(scores):
    '''Returns a function that gives the word score of a given word based on given scores.'''
    def helper2(word):
        if word == '':
            return 0
        return letterScore(word[0], scores) + helper2(word[1:])
    return helper2


def combine(wordList, scoreList):
    '''Returns a list of lists each containing a word and its associated word score.'''
    if wordList == [] or scoreList == []:
        return []
    return [ [ wordList[0], scoreList[0] ] ] + combine(wordList[1:], scoreList[1:])


def letterScore(letter, scorelist):
    '''Returns the score of a single given letter based on its value in scoreList'''
    if letter == scorelist[0][0]: #Checks if the letter is in the first pair
        return scorelist[0][1]
    return letterScore(letter, scorelist[1:]) #When letter is not in the first pair it recursively calls the next pair


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n].'''
    if L == []:
        return []
    if n == 0:
        return []
    return [ L[0] ] + take(n - 1, L[1:])



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:].'''
    if L == []:
        return []
    if n == 0:
        return [ L[0] ] + drop(n, L[1:])
    return drop(n-1, L[1:])










    
    
    
    
    
