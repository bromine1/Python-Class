
def mean(initial_list=[]):
    """
    Mean
    Takes an optional initial list, and an option for no input
    returns the average of the numbers
    
    """
    #import necessary modules
    import statistics
    #initialize list
    x = []
    for num in initial_list:
        x.append(num)
    #gather numbers, check for number
    while True:
        num = input("\nPlease input a number. If you are done, enter done: ")
        if num == "done":
            break
        try:
            fnum = float(num)
        except:
            print("Something went wrong")
            mean(x)
        # add number to list
        x.append(fnum)
    # Assign values to variable and print
    Mean = statistics.fmean(x)
    Median = statistics.median(x)
    print (f"your mean is {Mean} and your median is {Median}")

mean()