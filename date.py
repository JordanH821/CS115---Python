''' Created on _______________________ @author:   _______________________ Pledge:    _______________________
CS115 - Hw 11 - Date class ''' 
from _datetime import date
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
DAYS_IN_WEEK = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''
    # The constructor is always named __init__.     
    def __init__(self, month, day, year):         
        '''The constructor for objects of type Date.'''         
        self.month = month         
        self.day = day         
        self.year = year
        
        
    # The 'printing' function is always named __str__.     
    def __str__(self):         
        '''This method returns a string representation for the            
        object of type Date that calls it (named self).
        ** Note that this _can_ be called explicitly, but                 
        it more often is used implicitly via the print                 
        statement or simply by expressing self's value.'''         
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)
         
    # Here is an example of a 'method' of the Date class.     
    def isLeapYear(self):         
        '''Returns True if the calling object is in a leap year; False         
        otherwise.'''         
        if self.year % 400 == 0:             
            return True         
        if self.year % 100 == 0:             
            return False         
        if self.year % 4 == 0:             
            return True         
        return False

    def copy(self):
        '''Returns a new object with the same month, day, year
        as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew
    
    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
        whether or not they are the in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and \
            self.day == d2.day
            
    def tomorrow(self):
        '''Increments the date one day, tomorrow.'''
        changed = False
        if self.month == 2 and self.day == 29 and self.isLeapYear() == True:
            self.day = 1
            self.month = 3
            changed = True 
        if self.month == 2 and self.day == 28 and self.isLeapYear() == True:
            self.day = 29
            changed = True
        
        elif not changed:
            self.day += 1
            if self.day > DAYS_IN_MONTH[self.month]:
                self.day = self.day % DAYS_IN_MONTH[self.month]
                self.month += 1
            
            if self.month > 12:
                self.year += 1
                self.month = self.month % 12
        
    def yesterday(self):
        '''Increments the date backwards one day, yesterday.'''
        changed = False
        if self.day == 1:
            if self.month == 1:
                self.month = 12
                self.day = 31
                self.year = self.year - 1
                changed = True
                
            if self.month == 3 and self.isLeapYear() == True:
                self.day = 29
                self.month = 2
                changed = True
            elif not changed: 
                self.month = self.month - 1
                self.day = DAYS_IN_MONTH[self.month]
                changed = True
        if not changed:
            self.day = self.day -1
            
    def addNDays(self, N):
        '''Adds N days to the current date, prints the first date up to, and including the last day.'''
        for x in range(N):
            print(self)
            self.tomorrow()
        print(self)

        
    def subNDays(self, N):
        '''Subtracts N days to the current date, prints the first date up to, and including the last day.'''
        for x in range(N):
            print(self)
            self.yesterday()
        print(self)
        
    def isBefore(self, d2):
        '''Returns True if self date comes before d2 date, and false otherwise.'''
        if self.year == d2.year:
            if self.month == d2.month:
                if self.day == d2.day:
                    return False
                else:
                    return self.day < d2.day
            else:
                return self. month < d2.month
        else:
            return self.year < d2.year
        
        
    def isAfter(self, d2):
        '''Returns True if self date comes before d2 date, and false otherwise.'''
        if self.year == d2.year:
            if self.month == d2.month:
                if self.day == d2.day:
                    return False
                else:
                    return self.day > d2.day
            else:
                return self. month > d2.month
        else:
            return self.year > d2.year
        
    
    def diff(self, d2):
        '''Returns the number of days between two dates. The difference is positive
             if the self date is after d2 date, 0 if they are the same, and negative otherwise.'''
        diff = 0
        dateCopy = self.copy()
        if dateCopy.equals(d2):
            return diff
        elif dateCopy.isAfter(d2):
            while dateCopy.isAfter(d2):
                diff += 1
                dateCopy.yesterday()
            return diff
        else:
            while dateCopy.isBefore(d2):
                diff += -1
                dateCopy.tomorrow()
            return diff
        
    def dow(self):
        '''Returns the day of the week for a given date.'''
        COMPARE_DATE = Date(12, 7, 1941)
        diff = self.diff(COMPARE_DATE)
        if self.isBefore(COMPARE_DATE):
            dowNum = 6 - abs(diff) % 7
            return DAYS_IN_WEEK[dowNum]
        elif self.isAfter(COMPARE_DATE):
            dowNum = (6 + diff) % 7
            return DAYS_IN_WEEK[dowNum]
        else:
            return 'Sunday'

    