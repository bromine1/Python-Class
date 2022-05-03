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
finally:
    s.close() #Just in case

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
	for line in open('text.txt', 'rt'):
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
	fo = open('PracticeChallenges/Labs/Module8/Files/newfile.txt', 'w') # A new file (newtext.txt) is created.
	for i in range(10):
		s = "line #" + str(i+1) + "\n"
		for ch in s:
			fo.write(ch)
	fo.close()
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))

#writes lines for each line
#for some reason the example code returns an error, everything still works so it doesn't matter
