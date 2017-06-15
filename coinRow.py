'''
Created on Mar 16, 2016

@author: Test
'''
def coin_row(lst):
    if lst == []:
        return 0
    
    useIt = lst[0] + coin_row(lst[2:])
    loseIt = coin_row(lst[1:])
    return max(useIt, loseIt)

def coin_row_with_values(lst):
    if lst == []:
        return [ 0, [] ]
    
    useIt = coin_row_with_values(lst[2:])
    derp = [ useIt[0] + lst[0], useIt[1] + [lst[0]] ]
    loseIt = coin_row_with_values(lst[1:])
    loseIt = [ loseIt[0], loseIt[1]]
    
    if loseIt[0] > derp[0]:
        return loseIt
    return derp\
        
def fib(n):
    def fibMem(n, memo):
        if n in memo:
            return memo[n]
        
        if n == 0:
            result = 1
        elif n == 1:
            result = 1
        else:
            result = fibMem(n-1, memo) + fibMem(n-2, memo)
        memo[n] = result
        return result
    return fibMem(n, {})

def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n-1) + lucas(n-2)

def lucasMemo(n):
    def LM(n, memo):
        if n in memo:
            return memo[n]
        
        if n==0:
            result = 2
        elif n==1:
            result = 1
        else:
            result = LM(n-1, memo) + LM(n-2, memo)
        memo[n] = result
        return result
    return LM(n, {})

print(lucasMemo(70))

def LCS(s1, s2):
    if s1 == '' or s2 == '':
        return 0
    if s1[0] == s2[0]:
        return 1 + LCS(s1[1:], s2[1:])
    
    uses1 = LCS(s1, s2[1:])
    uses2 = LCS(s1[1:], s2)
    
    return max(uses1, uses2)
    


print(LCS('taaaco', 'blqlfaaaco'))
