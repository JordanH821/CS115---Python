'''
Created on Mar 24, 2016

@author: Jordan Handwerger

Pledge: I pledge my honor that I have abided by the Stevens Honor System. -JH
'''

def TcToNum(s):
    '''Returns the number represented by a two's-complement binary number'''
    if s[0] == '1':
        return -128 + binToNum(s[1:])
    return binToNum(s)


def binToNum(s):
    '''Returns the number represented in the binary string, s.''' 
    if s == '':
        return 0
    if s[0] == '0':
        return binToNum(s[1:])
    return binToNum(s[1:]) + int(s[0]) * (2 ** (len(s) - 1))


def NumToTc(num):
    '''Returns the two's-complement binary representation of a number.'''
    if num == 0:
        return '00000000'
    if num > 127 or num < -128:
        return 'Error'
    if num < 0:
        return '1' + padder(7, numToBinary((abs(128 + num))))
    return padder(8, numToBinary(num))


def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    if n%2==1:
        return numToBinary(n//2) + '1'
    return numToBinary(n//2) + '0'


def padder(padNum, s):
    '''Returns a new string padded with zeros until it is of given length padNum.'''
    if len(s) < padNum:
        return '0' * (padNum - len(s)) + s
    return s
    




    


