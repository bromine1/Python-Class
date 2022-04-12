# get list
# get list sort
# get sort by (alphabetical, numerical, length)
#output list in order with for loop

def getList():
    ListInput = True
    list = []
    # gets input and adds to list
    while ListInput:
        x = input("item to add to the list\n:")
        list.append(x)
        # prompt if finished?
        check = input("are you finished? \n [y]: yes\n [n] no\n:")
        if check.lower() == "y":
            ListInput=False
    return list

def getOrder():
    #gets sort order
    order = False
    while order == False:
        var= int(input("please select sort order:\n [1]: ascending\n[2]: descending\n:"))
        if var == 1 or var == 2:
            order = False
            return var
        else:
            print ("only input 1 or 2")
    return getOrder


# list sorter
def sortList(List, SortOrder):
    # establishes sort order
    x = List
    if SortOrder == 1:
        SList = sorted(x)
        return SList
    elif SortOrder == 2:
        x.reverse
        SList = sorted(x, reverse = True)
        return SList

def sortedList(list):
    # Gets sort order
    method = input("reverse order?\n [1] Yes\n[2] No\n: ")
    #establishes sort order
    if "1" in method:
        SList = sorted(list, reverse = True)
    elif "2" in method:
        SList = sorted(list)
    else:
        print("input error: please choose again")
        sortedList
    return SList

def ListSort():
    #Makes list and gets inputs
    list = []
    for x in range(int(input("how many list entries do you have?: "))):
        list.append(input("entry #{}: ".format(str(x+1))))
    # references sort order
    #prints list
    for x in sortedList(list):
        print (x)
ListSort()
exit
