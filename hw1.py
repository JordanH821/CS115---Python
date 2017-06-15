'''
Created on Jan 29, 2016

@author: Jordan Handwerger
'''
from cs115 import reduce, range

def mult(x, y):
    '''Returns the product of given x and y'''
    return x * y

def add(x,y):
    '''Returns the sum of given x and y'''
    return x + y

def factorial(n):
    '''Returns the factorial of a given positive integer n'''
    return reduce(mult, range(1, n+1))

def mean(L):
    '''Returns the mean of a given list of numbers'''
    return ( reduce(add, L) / len(L))



def divides(n):
    '''Returns a function that checks if n is divisible by a number k.'''
    def div(k):
        return n % k == 0
    return div


def prime(n):
    '''Returns True if the number is prime, or False if composite. Given a positive integer n.'''
    if n in [0,1]:
        return False
    elif True in (map(divides(n),(range(2,n)))):
        return False
    return True

print(list(map(prime, range(100))))
        

 


