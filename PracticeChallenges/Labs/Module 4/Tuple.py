# Tuples Practice, Ryan Stauffer & Acadia Baker

# Exercise 1: reverse the tuple
# expected output: (50, 40, 30, 20, 10)
print("exercise 1")
tuple1 = (10, 20, 30, 40, 50)
print(tuple1[::-1])

# Excercise 2: swap 2 tuples
#Expected output: 
#tuple1: (99, 88)
#tuple2: (11, 22)
print("exercise 2")

tuple1 = (11, 22)
tuple2 = (99, 88)
tempTuple = ()
tempTuple = tuple1
tuple1 = tuple2
tuple2 = tempTuple
print(tuple1)
print(tuple2)

#Excercise 3: Create a tuple with single item 150
print('exercise 3')
tuple150 = (150)
print(tuple150)


#Exercise 4
print('exercise 4')
tuple1 = (10, 20, 30, 40)
#assign variables
a = tuple1[0]
b = tuple1[1]
c = tuple1[2]
d = tuple1[3]
#print variables
print(a) # should print 10
print(b) # should print 20
print(c) # should print 30
print(d) # should print 40

#Exercise 5
print('exercise 5')
tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))