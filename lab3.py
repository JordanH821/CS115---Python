'''
Created on Feb 12, 2016

@author: Jordan Handwerger
'''

def change(target, numberList):
    '''Returns True if a numberList adds up to target, and False if not'''
    if target == 0:
        return 0
    elif numberList == []:
        return float("inf")
    elif numberList[0] > target:
        return change(target, numberList[1:])
    useIt = 1 + change(target-numberList[0], numberList)
    loseIt = change(target, numberList[1:])
    return min(useIt,loseIt)
    
