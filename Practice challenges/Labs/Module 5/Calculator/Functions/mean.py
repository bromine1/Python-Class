
def mean():
    """
    Mean
    Takes an optional initial list, and an option for no input
    returns the average of the numbers
    
    """
    #import necessary modules
    import statistics
    x = []
    while True:
        num = input("\nPlease input a number. If you are done, enter done: ")
        if num == "done":
            break
        try:
            fnum = float(num)
        except:
            print("Something went wrong")
            mean()
        x.append(fnum)
    Mean = statistics.fmean(x)
    Median = statistics.median(x)
    print (f"your mean is {Mean} and your median is {Median}")

mean()