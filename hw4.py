'''
Created on Feb 19, 2016

@author: Jordan Handwerger
Pledge: I pledge my honor that I have abided by the Stevens Honor System. - JH
'''
def pascal_row(n):
    '''Returns the nth row in Pascal's Triangle'''
    if n == 0:
        return [1] 
    return add_ones(next_pascal(pascal_row(n-1)))


def next_pascal(lst):
    '''Returns next row of Pascal's Triangle, without the ones,
        given a list of the previous row.''' 
    if lst == [] or len(lst) == 1:
        return []
    return [lst[0] + lst[1]] + next_pascal(lst[1:])

def add_ones(lst):
    '''Returns the given lst with [1] concatenated on both ends.'''
    return [1] + lst + [1]

def pascal_triangle(n):
    '''Returns a list of lists of each Pascal Row up to and including n.'''
    if n == 0:
        return [[1]]
    return pascal_triangle(n-1) + [ pascal_row(n) ]


print(pascal_triangle(4))






