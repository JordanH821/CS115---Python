'''
Created on Feb 5, 2016

@author: Jordan Handwerger
'''
def dot(L, K):
    ''' Calculates the dot product of L and K'''
    if L == [] or K == []:
        return 0
    return (L[0] * K[0]) + dot(L[1:], K[1:])

def explode(S):
    '''Returns a list with each letter of S separated'''
    if S == '':
        return []
    elif type(S) == list:
        return S
    return [ S[0] ] + explode(S[1:])

def ind(e, L):
    '''Returns the index of e inside L'''
    if L == [] or L == '':
        return 0
    elif e == L[0]:
        return 0
    return 1 + ind(e, L[1:])

def removeAll(e, L):
    '''Removes all top level instances of L'''
    if L == []:
        return []
    elif e == L[0]:
        return removeAll(e, L[1:])
    return [ L[0] ] + removeAll(e, L[1:])
        
def myFilter(f, lst):
    '''Applies a function f to a list, lst'''
    if lst == []:
        return []
    elif f(lst[0]) == True:
        return [ lst[0] ] + myFilter(f, lst[1:])
    return myFilter(f, lst[1:])

def deepReverse(L):
    '''Returns the list L with all instances reversed in order'''
    if L == []:
        return []
    elif type(L[0]) == list: # or isinstance(L[0], list)
        return deepReverse(L[1:]) + [ deepReverse(L[0]) ]
    return deepReverse(L[1:]) + [ L[0] ]


