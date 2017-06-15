'''
Created on March 2. 2016
@author:  Jordan Handwerger
Pledge:   I pledge my honor that I have abided by the Stevens Honor System. -JH
CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
from lab6 import numToBinary
from cs115 import reduce
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

# Question 1.) The longest possible number of bits to encode a 64-bit image is 7, which its highest run length is 7**2 -1 = 127. 2 **6 would not be enough if 
# the given sting was all 1's or 0's because 2**6 -1 = 63 and you cannot represent 64 with 63.

# Question 2.) All compressions with greater than 3 consecutive numbers in a row can smaller than their uncompressed base s, with the correct compressed 
# block size. ex.) 111 can be represented as 11 in binary. As the consecutive numbers increase higher the ratio gets smaller.

# Question 3.) This compression algorithm is impossible because an alternating 64 bit string has to be represented by at least a 64 bit string to maintain the 
# bit order.

def consec_count(s):
    '''Returns the number of times the first character of a given string, s, appears consecutively.'''
    if s == '':
        return 0
    if len(s) == 1:
        return 1
    if s[0] == s[1]:
        return 1 + consec_count(s[1:])
    else:
        return 1
    
def consec_all(s):
    '''Returns the a list of the numbers of consecutive repeats of a character for each new character in the given string, s.'''
    if s == '':
        return []
    return [consec_count(s)] + consec_all(s[consec_count(s):])

def num_breaker(lst):
    '''Returns a list with all values greater than the MAX_RUN_LENGTH broke into pieces smaller than or equal to the MAX_RUN_LENGTH'''
    if lst == []:
        return []
    if lst[0] > MAX_RUN_LENGTH:
        lst[0] = lst[0] - MAX_RUN_LENGTH
        return [MAX_RUN_LENGTH, 0] + num_breaker(lst)
    return [lst[0]] + num_breaker(lst[1:])

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

def zero_fill(n):
    '''Returns a list of strings of numbers padded with zeros so they are all have the length of the COMPRESSED_BLOCK_SIZE.''' 
    if len(n) < COMPRESSED_BLOCK_SIZE:
        return '0' * (COMPRESSED_BLOCK_SIZE - len(n)) + n
    return n

def add(x, y):
    '''Returns x added to y.'''
    return x + y

def compress(s):
    '''Returns a new string that is a compression og the given string, s.'''
    if s[0] == '1':
        return '0' * COMPRESSED_BLOCK_SIZE + reduce(add, (map(zero_fill, (list(map(numToBinary, num_breaker(consec_all(s))))))))
    return reduce(add, (map(zero_fill, (list(map(numToBinary, num_breaker(consec_all(s))))))))

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    def bin_help(n, snum):
        if n == '':
            return 0
        return int(n[-1]) * (2 ** snum) + bin_help(n[:-1], snum+1)
    return bin_help(s, 0)


def uncompress(c):
    '''Returns a function that uncompresses a string, c'''
    def uncompress_help(c, n):
        if c == '':
            return ''
        if n % 2 == 0:
            return '0' * binaryToNum(c[:5]) + uncompress_help(c[5:], n+1)
        return '1' * binaryToNum(c[:5]) + uncompress_help(c[5:], n+1)
    return uncompress_help(c, 0)

def compression(s):
    '''Returns the ratio of the length of compressed string to uncompressed string.'''
    return len(compress(s))/len(s)

