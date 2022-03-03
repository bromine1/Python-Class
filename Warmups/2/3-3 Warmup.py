#Import Modules
import random as r
# Define Funcion
def wacky(init=[]):
    #initiallize and append inputted data
    nums = []
    for x in init:
        nums.append(x)
    # clause to get numbers and check if 
    start = r.randint(1,1000)
    #Use start here to prevent value error
    stop = r.randint(start,1000 + start)
    for x in range(start, stop):
        nums.append(x)
    while True:
        #Get the sample range, and check to prevent an IndexError
        sampleRange = r.randint(1,30)
        if sampleRange <= stop - start:
            break
    #Return wacky value
    return r.sample(nums, k=sampleRange)

print(wacky())
exit()