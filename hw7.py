'''
Created on Mar 11, 2016

@author: Jordan Handwerger

Pledge: I pledge my honor that I have abided by the Stevens Honor System. - JH
'''
FullAdder = \
{ ('0','0','0') : ('0','0'),
('0','0','1') : ('1','0'),
('0','1','0') : ('1','0'),
('0','1','1') : ('0','1'),
('1','0','0') : ('1','0'),
('1','0','1') : ('0','1'),
('1','1','0') : ('0','1'),
('1','1','1') : ('1','1') }

# The test cases for numToBaseB return '0' for N = 0, then at the 
# end of the section the hint says to return an empty string


def numToBaseB(N, B):
    '''Return the number N, given in decimal, in given base B, from base 2 to 10.'''
    if N == 0:
        return '0'
    if N//B == 0:
        return str(N % B)
    return numToBaseB(N//B, B) + str(N % B)


def baseBToNum(S, B):
    '''Returns a function that returns S, a number represented in binary,
     in a new base base B, from base 2 to 10.'''
    def BToNumHelp(S, B, n):
        if S == '':
            return 0
        return int(S[-1]) * B ** n + BToNumHelp(S[:-1], B, n+1)
    return BToNumHelp(S, B, 0)


def baseToBase(B1, B2, sinB1):
    '''Returns a string of in base, B2, given a string, sinB1, in base B1.'''
    return numToBaseB(baseBToNum(sinB1, B1), B2)


def add(B1, B2):
    '''Returns the sum of binary numbers B1 and B2 in binary.'''
    return numToBaseB(baseBToNum(B1, 2) + baseBToNum(B2, 2), 2)


def addB(B1, B2):
    '''Returns a function that returns the binary sum,
         of the binary numbers B1 and B2.'''
    if len(B1) < len(B2):
        return addB((len(B2) - len(B1)) * '0' + B1, B2)
    if len(B2) < len(B1):
        return addB(B1, (len(B1) - len(B2)) * '0' + B2) 
    
    def addHelp(B1, B2, carry):
        if B1 == '' and B2 == '' and carry == '0':
            return ''
        if B1 == '' and B2 == '' and carry == '1':
            return '1'
        sumCar = FullAdder[(B1[-1:], B2[-1:], carry)]
        return addHelp(B1[:-1], B2[:-1], sumCar[1]) + sumCar[0] 
    return addHelp(B1, B2, '0')





    

        