# Resturaunt menu assignment Ryan Stauffer & Acadia Baker
# Tuber Tavern
#Establish Menu
menu = ('potato soup', 'mashed potato', 'fries', 'baked potato', 'sweet potato')
#Print Items
for item in menu:
    print (item)
#Try and add menu items
try:
    menu.append("Apple Pie")
except AttributeError:
    print("\nWe only serve tubers\n")
#New Menu Items
newmenu = ('potato chips', 'latkes')
# Make new menu
menu = newmenu + menu[0:3]
#print menu items
for item in menu:
    print (item)
exit()