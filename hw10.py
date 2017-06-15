'''
Created on Apr 13, 2016

@authors: Jordan Handwerger and Chris Landolfi 
Pledge: I pledge my honor that I have abided by the Stevens Honor System.

'''
PREF_FILE = "musicrecplus.txt"
# A very simple music recommender system.

    

def loadUsers(fileName):
    ''' Reads in a file of stored users' preferences
        stored in the file 'fileName'.
        Returns a dictionary containing a mapping
        of user names to a list preferred artists
    '''
    file = open(fileName, 'r')
    userDict = {}
    for line in file:
        # Read and parse a single line
        [userName, bands] = line.strip().split(":")
        bandList = bands.split(",")
        bandList.sort()
        userDict[userName] = bandList
    file.close()
    return userDict

         
def getPreferences(userName, userMap):
    ''' Returns a list of the uesr's preferred artists.

        If the system already knows about the user,
        it gets the preferences out of the userMap
        dictionary and then asks the user if she has
        additional preferences.  If the user is new,
        it simply asks the user for her preferences. '''
    newPref = ""
    if userName in userMap:
        prefs = userMap[userName]
        print("I see that you have used the system before.")
        print("Your music preferences include:")
        for artist in prefs:
            print(artist)
        print("Please enter another artist or band that you")
        print("like, or just press enter")
        newPref = input("to see your recommendations: ")
    else:
        prefs = []
        print("I see that you are a new user.")
        print("Please enter the name of an artist or band")
        newPref = input("that you like: " )
        
    while newPref != "":
        prefs.append(newPref.strip().title())
        print("Please enter another artist or band that you")
        print("like, or just press enter")
        newPref = input("to see your recommendations: ")
    
    print(getRecommendations(userName, prefs, userMap))
        
    # Always keep the lists in sorted order for ease of
    # comparison
    prefs.sort()
    return prefs


def getRecommendations(currUser, prefs, userMap):
    '''Gets recommendations for a user (currUser) based
        on the users in userMap (a dictionary)
        and the user's preferences in pref (a list).
        Returns a list of recommended artists.'''
    bestUser = findBestUser(currUser, prefs, userMap)
    recommendations = drop(prefs, userMap[bestUser])
    return recommendations
 

def findBestUser(curretUser, prefs, userMap):
    """Returns the user with the most common prefs as the current User"""
    users = list(userMap.keys())
    bestScore = -1
    bestMatch = None
    for user in users:
        score = numMatches(prefs, userMap[user])
        if prefs != userMap[user]:
            if score > bestScore:
                bestScore = numMatches(prefs, userMap[user])
                bestMatch = user
    return bestMatch

def drop(list1, list2):
    '''Return a new list that contains only the elements in
        list2 that were NOT in list1. '''
    list3 = []
    for i in list2:
        if i not in list1:
            list3 += [i]
    return list3

def numMatches( list1, list2 ):
    ''' return the number of elements that match between
        two sorted lists '''
    same = 0
    for i in list1:
        if i in list2:
            same += 1
    return same

def saveUserPreferences(userName, prefs, userMap, fileName):
    ''' Writes all of the user preferences to the file.
        Returns nothing. '''
    userMap[userName] = prefs
    file = open(fileName, "w")
    for user in userMap:
        toSave = str(user) + ":" + ",".join(userMap[user]) + \
                    "\n"
        file.write(toSave)
    file.close()

def artistList(userMap):
    '''Returns a list of artists, filtered so every artist only appears once.'''
    artistList = []
    filteredList = []
    for user in userMap:
        artistList += userMap[user]
    for artist in artistList:
        if artist not in filteredList:
            filteredList += [artist]
    return filteredList



def listToDict(lst):
    '''Converts the list of artist to a dictionary each associated with 0 occurences'''
    artistDict = {}
    for i in lst:
        artistDict[i] = 0
    return artistDict

            
         


def mostPopular(file):
    '''returns the most popular artist in the given group of users in the file.'''
    artDict = listToDict(artistList(loadUsers(file)))
    userMap = loadUsers(file)
    for user in userMap:
        for artist in userMap[user]:
            artDict[artist] += 1
    x = 0
    y = ''
    for artist in list(artDict.keys()):
        if artDict[artist] > x:
            x = artDict[artist]
            y = artist
    return y

def howPopular(file):
    '''Returns the number of users who like the most popular artist.''' 
    artDict = listToDict(artistList(loadUsers(file)))
    userMap = loadUsers(file)
    for user in userMap:
        for artist in userMap[user]:
            artDict[artist] += 1
    x = 0
    for artist in list(artDict.keys()):
        if artDict[artist] > x:
            x = artDict[artist]
    return x


def mostLikes(fileName):
    '''Returns the user with the most likes, unless their name ends with '$', opting them out.'''
    userMap = loadUsers(fileName)
    x = 0
    for user in userMap:
        if user[-1] != '$':
            if len(userMap[user]) > x:
                x = len(userMap[user])
                y = user
    return y
            

            
def main():
    ''' The main recommendation function '''
    userMap = loadUsers(PREF_FILE)
    print("Welcome to the music recommender system!\n")

    userName = input("Please enter your name: ")
    print ("\nWelcome,", userName, '\n')
    
    while True:
        option = input('Enter a letter to choose an option:' + '\n' + '\t' + 'e - enter preferences' + '\n' + '\t' 'r - get recommendations' + '\n' + '\t' \
           + 'p - show most popular artists'  + '\n' + '\t' + 'h - how popular is the most popular' + \
           '\n' + '\t' + 'm - which user has the most likes ' + '\n' + '\t' + 'q - save and quit')
        if option == 'e':
            prefs = getPreferences(userName, userMap)
            saveUserPreferences(userName, prefs, userMap, PREF_FILE)
            
        if option =='r':
            try:
                print(getRecommendations(userName, userMap[userName], userMap))
            except:
                print("\nYou need to enter preferences first. \n")
            
        if option == 'p':
            print(mostPopular(PREF_FILE))
        
        if option == 'h':
            print(howPopular(PREF_FILE))
            
        if option == 'm':
            print(mostLikes(PREF_FILE))
            
        if option == 'q':
            return None
        
        if option not in ['e', 'r', 'p', 'h', 'm', 'q']:
            print("That is not an option.")
            
    

if __name__ == "__main__": main()