# Modules needed for code
# This was really an excuse for me to exercise regex
from re import split, search, findall
from os import strerror



class StudentsDataException(Exception): #Base exception class
    pass


class BadLine(StudentsDataException):
    def __init__(self, lineNumber, erroneousLine: object) -> None: #Gathers values to report error
        super().__init__(self)
        self.line = lineNumber
        self.errorLine = erroneousLine


class FileEmpty(StudentsDataException):
    def __init__(self: object) -> None:
        super().__init__()


file = input("Please give a complete path to the file")
#Below is a sample file used for testing
# file = 'PracticeChallenges/Labs/Module8/Files/DataSample.txt'
studentData = {} #initialize data dictionary

# Open file and grab data
try:
    with open(file, 'r', encoding='UTF-8') as data:
        data = data.readlines() #store the data in readlines, we only need to read it once
except IOError as e:
    print(f" IOError: {strerror(e.errno)}")

# Verify data as usable
try:
    if data == []:
        raise FileEmpty
    count = 0
    for line in data:
        count += 1
        if search("\w+\s\w+\s(\d+.?\d*)", line) == None: # Detects proper format
            raise BadLine(count, line) # returns line errored on and line content
except BadLine as e:
    print(f"Bad Line: Line number {e.line}, erroneous content:\n{e.errorLine}")
except FileEmpty:
    print(f'File "{file}" is empty')


try:
    dataList = split("\t", line) #Split by spaces
    studentData[f"{dataList[1]}, {dataList[0]}"] += int(findall("(\d+.?\d*)",dataList[2])[0])
    # Above grabs the student's first and last name and adds the received value
    # Regex grabs the number while leaving behind the newline character
    # the [0] is because findall returns a list, even if there is only one match
except KeyError:
    studentData.update({f"{dataList[1]}, {dataList[0]}": float(findall("(\d+.?\d*)",dataList[2])[0])})
    #Same as before, except it adds the student if it isn't there

print("Final Values") # Nice little table with nice little formating
for student in sorted(studentData):
    print(f"{student}:".rjust(12), end=" ")
    print(f"{studentData[student]} points".ljust(5))