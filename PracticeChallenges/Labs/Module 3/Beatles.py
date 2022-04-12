#Ryan Stauffer lab 3.4.1.13

# step 1
#Establish the List
beatles = []

print("Step 1:", beatles)

# step 2
# add the members
initial_members = ["John Lennon", "Paul McCartney", "George Harrison"]
for member in initial_members:
    beatles.append(member)

print("Step 2:", beatles)

# step 3
#use for loop to grab user input. IDK why they asked for unchecked input, but they asked for it
for member in range(2):
    beatles.append(input("input Stu Sutcliffe now, then input Pete Best next\n:"))
print("Step 3:", beatles)

# step 4

#Delete the last input. Why even ask?
del beatles[-2:]

print("Step 4:", beatles)

# step 5
#add Ringo Starr
beatles.insert(0, "Ringo Starr")

print("Step 5:", beatles)


# testing list length
print("The Fab", len(beatles))
