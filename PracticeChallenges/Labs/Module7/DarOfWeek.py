class WeekDayError(KeyError):
    pass
	

class Weeker:
    #Reference tables for days and weeks
    __numToWeek = {
        1 : 'Sun',
        2 : 'Mon',
        3 : 'Tue',
        4 : 'Wed',
        5 : 'Thu',
        6 : 'Fri',
        7 : 'Sat'
    }
    __weekToNum = {
        'Sun' : 1,
        'Mon' : 2,
        'Tue' : 3,
        'Wed' : 4,
        'Thu' : 5,
        'Fri' : 6,
        'Sat' : 7,
    }

    def __init__(self, day): #get start date
        try:
            self.__day = Weeker.__weekToNum[day]
        except KeyError:
            raise WeekDayError


    def __str__(self): #Account for date starting from 7 backwards and return it
        for dayOfWeek in reversed(range(1, 8)):
            if self.__day % dayOfWeek == 0:
                return(str(Weeker.__numToWeek[dayOfWeek]))

    def add_days(self, n): # add days
        self.__day += n % 7
        #Modulous is needed to prevent numbers from getting large
        #this should keep numbers in an acceptable range for __str__

    def subtract_days(self, n): #subtracts days
        self.__day -= n % 7
        #Modulous is needed to prevent numbers from getting large
        #this should keep numbers in an acceptable range for __str__

try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")