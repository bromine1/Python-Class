# Establish List
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# Establish Working List
final_list = []

#Iterate through list. If found in the list, it will continue
# Otherwise, it will add to the list
for i in my_list:
    if i in final_list:
        continue
    final_list.append(i)

#Syncs Client list with working List
my_list = final_list

#Prints the list
print("The list with unique elements only:")
print(my_list)
