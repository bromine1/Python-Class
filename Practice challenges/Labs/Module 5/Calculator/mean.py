
# def mean(initial=[], noInput = False):
#     """
#     Mean
#     Takes an optional initial list, and an option for no input
#     returns the average of the numbers
    
#     """
#     #import necessary modules
#     import decimal
#     x = []
#     x.append(number for number in initial)
#     if noInput == True:
#         while True:
#             num = input("\nPlease input a number. If you are done, just hit enter")
#             if x == "":
#                 break
#             try:
#                 decimal(num)
#             except:
#                 print("Something went wrong")
#                 mean(initial=x)
#             if x == "":
#                 break
#             else:
#                 x.append(num)
#     return sum(x) / len(x)

def mean(list):
    return sum(list)/mean(list)