''' Created on _Feb 5, 2016________ @author:   _Jordan Handwerger__Christoher Landolfi_______ Pledge:    __"I pledge my honor that I have abided by the Stevens Honor System." -JH -CL
CS115 - Hw 2 ''' 
import sys 
from cs115 import filter # Be sure to submit hw2.py.  Remove the '_template' from the file name.
# Allows up to 10000 recursive calls. # The maximum permitted limit varies from system to system. 
sys.setrecursionlimit(10000)
# Leave the following lists in place. 
scrabbleScores =    [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
                        ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
                        ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
                        ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]
Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo', 'spam', 'spammy', 'zzyzva']
# Implement your functions here.
     
def letterScore(letter, scorelist):
    '''Returns the score of a single given letter based on its value in scoreList'''
    if letter == scorelist[0][0]: #Checks if the letter is in the first pair
        return scorelist[0][1]
    return letterScore(letter, scorelist[1:]) #When letter is not in the first pair it recursively calls the next pair

def wordScore(S, scorelist):
    '''Returns the total value of all letters in a given string, S, based on the values in scoreList'''
    if S == '': #Base case when S is an empty string it will return 0, the value of empty
        return 0
    return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist) #adds first letter score to the recursively called second letter score


def poss(letters):#Function is used to test if any words in the global dictionary can be made out of the letters in Rack
    '''Returns a function, work, that checks if a given word can be made with the given letters'''
    def work(word):
        if word == '': #Base case in case an empty list is given as a word
            return True
        elif type(word) == str: #Changes a word given as a string into a list of its letters to use the .remove() function
            word = list(word)
        elif word == []: #Since after the first call word is a list, when it is empty the word would have been valid with the given letters
            return True 
        elif letters == []: #word is too long for the given letters, and has used the whole list
            return False
    
        if letters[0] in word:  # if the first letter in letters is in the word, the function removes that letter from word and calls letters without that value 
            word.remove(letters[0]) #Fixes error where any letter in a letters would allow infinite instances of itself 
            return poss(letters[1:])(word)
        return poss(letters[1:])(word)
    return work #allows for nested function


def combine(lst): 
    '''Returns a list of lists of each word and its associated score'''
    if lst == []: #Base case: list is empty is has associated all words with their score
        return []
    return [[ lst[0], wordScore(lst[0], scrabbleScores) ]] + combine(lst[1:]) #recursive call


def scoreList(rack):
    '''Returns the list of all possible words and their scores based on the given rack'''
    return combine(filter(poss(rack), Dictionary)) #Filters the possible words then combines them


def best_word_help(lst):
    '''Returns the word score pair with the highest score'''
    if lst == []: #base case if an empty list is entered
        return ['', 0] 
    if len(lst) == 1: #Base Case #2 if there is one element in a list it has to be the highest
        return lst[0]
    elif lst[0][1] > lst[1][1]: #Recursively finds the largest value, replaces smaller values with larger
        lst[1] = lst[0]
        return best_word_help(lst[1:])
    return best_word_help(lst[1:])


def bestWord(Rack):
    '''Returns the highest possible scoring word in the rack'''
    return best_word_help(scoreList(Rack)) #Calls helper function
 


