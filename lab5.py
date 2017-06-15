'''
Created on February 26, 2016
@author:   Jordan Handwerger
Pledge:    I pledge my honor that I have abided by the Stevens Honor System. -JH

CS115 - Lab 5
'''
import time

from cs115 import map

words = []
HITS = 10

def fastED(first, second):
    '''Returns the edit distance between the strings first and second. Uses
    memoization to speed up the process.'''
    def fast_helper(s1, s2, memo):
        if (s1, s2) in memo:
            return memo[(s1, s2)]
        
        if s1 == '':
            result = len(s2)
        elif s2 == '':
            result = len(s1)
        elif s1[0] == s2[0]:
            result = fast_helper(s1[1:], s2[1:], memo)
        else:
            substitution = 1 + fast_helper(s1[1:], s2[1:], memo)
            deletion = 1 + fast_helper(s1[1:], s2, memo)
            insertion = 1 + fast_helper(s1, s2[1:], memo)
            result = min(substitution, deletion, insertion)
        memo[(s1, s2)] = result 
        return result
    return fast_helper(first, second, {}) 


def getSuggestions(user_input):
    '''For each word in the global words list, determine the edit distance of
    the user_input and the word. Return a list of tuples containing the
    (edit distance, word).
    Hint: Use map and lambda, and it's only one line of code!'''
    return map(lambda x: (fastED(x, user_input), x), words)

def spam():
    '''Main loop for the program that prompts the user for words to check.
    If the spelling is correct, it tells the user so. Otherwise, it provides up
    to HITS suggestions.

    To exit the loop, just hit Enter at the prompt.'''
    while True:
        user_input = input('spell check> ').strip()
        if user_input == '':
            break
        if user_input in words:
            print('Correct')
        else:
            start_time = time.time()
            suggestions = getSuggestions(user_input)
            suggestions.sort()
            endTime = time.time()
            print('Suggested alternatives:')
            for suggestion in suggestions[:HITS]:
                print(' %s' % suggestion[1])
            print('Computation time:', endTime - start_time, 'seconds')
    print('Bye')

if __name__ == '__main__':
    f = open('3esl.txt')
    for word in f:
        words.append(word.strip())
    f.close()
    spam()