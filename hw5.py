'''
Created on March 1, 2016
@author:   Jordan Handwerger
Pledge:    I pledge my honor that I have abided by the Stevens Honor Sytstem. -JH

CS115 - Hw 5
'''
import turtle  # Needed for graphics

# Ignore 'Undefined variable from import' errors in Eclipse.

def svTree(trunkLength, levels):
    '''Draws a tree with the given trunk length and levels.'''
    if levels == 0:
        return 
    turtle.forward(trunkLength)
    turtle.left(30)
    svTree(trunkLength/2, levels-1)
    turtle.right(60)
    svTree(trunkLength/2, levels-1)
    turtle.left(30)
    turtle.backward(trunkLength)
    
    

def fastLucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    def fast_helper(n, memo):
        if n in memo:
            return memo[n]
        
        if n == 0:
            result = 2
        elif n == 1:
            result = 1
        else:
            result = fast_helper(n-1, memo) + fast_helper(n-2, memo)
        memo[n] = result
        return result
    return fast_helper(n, {})
# If you did this correctly, the results should be nearly instantaneous.
print(fastLucas(3))  # 4
print(fastLucas(5))  # 11
print(fastLucas(9))  # 76
print(fastLucas(24))  # 103682
print(fastLucas(40))  # 228826127
print(fastLucas(50))  # 28143753123

# Should take a few seconds to draw a tree.
svTree(128, 6)
