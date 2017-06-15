'''
Created on Feb 19, 2016

@author: Jordan Handwerger
Pledge: I pledge my honor that I have abided by the Stevens Honor System - JH
'''

def knapsack(weight, itemList):
    '''Returns a list of the maximum value achievable,given the weight,
     and a list of the items that make up this maximum value.'''
    if weight == 0: 
        return [0, []]
    if itemList == []:
        return [0, []]
    
    if weight < itemList[0][0]:
        return knapsack(weight, itemList[1:])
    useIt = knapsack(weight - itemList[0][0], itemList[1:])
    useIt = [ itemList[0][1] + useIt[0], [ itemList[0] ] + useIt[1]  ]
    loseIt = knapsack(weight, itemList[1:])
    if loseIt[0] > useIt[0]:
        return loseIt
    return useIt
