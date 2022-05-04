from os import strerror
#counts characters


#Read(int) reads the given number of characters at a time. The default is all characters
try:
    cnt = 0
    s = open('PracticeChallenges/Labs/Module8/Files/sample.txt', "rt")
    ch = s.read(1) #Read 1 character at a time
    while ch != '':
        print(ch, end='')
        cnt += 1
        ch = s.read(1)
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

#readline() lets us read lines individually in python
#You can pass it an integer to specify how many bites you want
try:
    ccnt = lcnt = 0
    s = open('PracticeChallenges/Labs/Module8/Files/sample.txt', 'rt')
    line = s.readline()
    while line != '':
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
        line = s.readline()
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


#Files are also an iterable, and as such can be used with items like for()
#You iter over a line
try:
    ccnt = lcnt = 0
    for line in open('PracticeChallenges/Labs/Module8/Files/sample.txt', 'rt'):
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

#We can write to files too

try:
    fo = open('PracticeChallenges/Labs/Module8/Files/newfile.txt', 'w')  # A new file (newtext.txt) is created.
    for i in range(10):
        s = "line #" + str(i+1) + "\n"
        for ch in s:
            fo.write(ch)
    fo.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

#writes lines for each line
#for some reason the example code returns an error, everything still works so it doesn't matter


# There are also byte arrays, or containers that store lots of bytes
# Byte arrays can be initialised with bytearray(), and only give you as many bytes as you give it
data = bytearray(10)
# name = func(number of bytes)
#
for i in range(len(data)):
    data[i] = 10 - i # Makes sure bytes aren't all zeroes

for b in data:
    print(hex(b))  # Converts byte data to hexadecimal


data = bytearray(ord('0'))


for i in range(len(data)):
    data[i] = 10 + i

try: #write data into file
    bf = open('PracticeChallenges/Labs/Module8/Files/file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

with open('PracticeChallenges/Labs/Module8/Files/file.bin', 'rb') as bf:
    data = bytearray(ord('a')) #rezero the code
    print(data)
    bf.readinto(data) #read the data
    print(data)
try:
    print(data)
    for b in data:
        print(hex(b), end=' ') #print it in hexadecimal for readability
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# We can also use the .read(int) method, where int is the number of bytes we wish to read

#Example of Practical use
srcname = input("Enter the source file name: ") #source name



try:
    src = open(srcname, 'rb') #Open as byte file
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)	

dstname = input("Enter the destination file name: ") #destination name
try:
    dst = open(dstname, 'wb') #open as byte file
except Exception as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    src.close()
    exit(e.errno)	

buffer = bytearray(65536) #byte buffer, reads 64 kb at a time
total  = 0
try:
    readin = src.readinto(buffer) #reads 64 kb into memory
    while readin > 0: 
        written = dst.write(buffer[:readin]) #writes 64 kb into memory
        total += written #tally up bytes
        readin = src.readinto(buffer) #reads next 64 kb
except IOError as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    exit(e.errno)	
    
print(total,'byte(s) succesfully written')
src.close()
dst.close()
