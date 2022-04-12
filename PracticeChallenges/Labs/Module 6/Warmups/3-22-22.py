#Ryan S 3-22-22 warmup

# Demonstrating operations on a string:
str1 = 'a'
str2 = 'b'

print(str1 + str2)
# outputs ab
print(str2 + str1)
#outputs ba
print(5 * 'a')
#outputs aaaaa
print('b' * 4)
# outputs bbbb

# gets the unicode character of period
print(chr(ord(".")))
#Prints the unicode character above period
print(chr(ord(".")+1))
#Prints the unicode character below period
print(chr(ord(".")-1))


# Demonstrating the in and not in operators function by providing two examples of each.

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
def realMonth(testMonth):
    if testMonth in months:
        return "That is a real month"
    if testMonth not in months:
        return "That is not a real month"

print (realMonth("March"))
print (realMonth("Logsday"))