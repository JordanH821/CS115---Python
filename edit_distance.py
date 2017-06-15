'''
Created on Feb 22, 2016

@author: Test
'''

'''def ed(str1, str2):
    if str1 == str2:
        return 0 
    if str1[0] != str2[0]:
        if len(str1) > len(str2):
            str2 += str1[0] + str2
            return 1 + ed(str1[1:], str2[1:])
        if len(str1) == len(str2):
            str2[0] = str1[0]
            return 1 + ed(str1[1:])'''
            
            
def ed(first, second):
    if first == '':
        return len(second)
    if second == '':
        return len(first)
    if first[0] == second[0]:
        return ed(first[1:], second[1:])
    substitution = 1 + ed(first[1:], second[1:])
    deletion = 1 + ed(first[1:], second)
    insertion = 1 + ed(first, second[1:])
    return min(substitution, insertion, deletion)

            
