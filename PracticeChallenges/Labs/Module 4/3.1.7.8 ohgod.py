def is_year_leap(year):
    # Check if Leap Year
	if year % 100 == 0:
		if year % 400 == 0:
			return True
		else:
			return False
	elif year % 4 == 0:
		return(True)
	else:
		return(False)

def days_in_month(year, month):
    # Figure out the days in a given month
    days= [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #check if leap year
    if is_year_leap(year):
        days[2] = 29
    return(days[month])

def day_of_year(year, month, day):
    # add the number of days in the number days in previous months plus a different number of days
    if not (isinstance(year, int)) or not( isinstance(month, int) and (month > 0 and month < 13) or not(isinstance(day, int) and (day > 0 and day < 32))):
        return None
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year):
        days[2] = 29
    return sum (days[:month]) + day
# test data
print(day_of_year(2000, 12, 31),"days have passed")
print(day_of_year(1900, 1, 13),"days have passed")
print(day_of_year(2016, 5, 25),"days have passed")
print(day_of_year(2087, 7, 12),"days have passed")
exit()
