'''
Created on Jan 29, 2016

@author: Test
'''
from cs115 import map, reduce, range
from math import factorial
import math 

def inverse(n):
    '''Returns the inverse of a given number n'''
    return float(1/n)

def add(x,y):
    '''Returns the sum of a given x and y'''
    return x+y

def e(n):
    '''Returns the Taylor approximation of e to a given number n'''
    return reduce(add, map(inverse, (map(factorial, range(n+1)))))

def error(n):
    '''Returns the error in a Taylor approximation to given n-th order of e'''
    return abs((math.e - e(n)))


print(e(10))