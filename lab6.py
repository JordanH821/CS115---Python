'''
Created on March 4, 2016
@author: Jordan Handwerger
Pledge:    I pledge my honor that I have abided by the Stevens 
            Honor System. -JH

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n % 2 == 0:
        return False
    return True

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    if isOdd(n):
        return numToBinary(n//2) + '1'
    return numToBinary(n//2) + '0'
  
        
    

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    def bin_help(n, snum):
        if n == '':
            return 0
        return int(n[-1]) * (2 ** snum) + bin_help(n[:-1], snum+1)
    return bin_help(s, 0)
    

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    if s == '11111111':
        return '00000000'
    elif s[-1] == '0':
        return s[:-1] +'1'
    return increment(s[:-1]) + '0'


def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n == 0:
        print(s)
        return ''
    print(s)
    return count(increment(s), n-1)

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    if n % 3 == 0:
        return numToTernary(n//3) + '0'
    return numToTernary(n//3) + str(n%3)


def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    def tern_help(s, snum):
        if s == '':
            return 0
        return int(s[-1]) * (3 ** snum) + tern_help(s[:-1], snum+1)
    return tern_help(s, 0)


        
        
        
        
        
        
        
        
