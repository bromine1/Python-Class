#Processing Files in Python

#File Handling Classwork
#Things of Note

#Windows file systems:
# - case insensitive
# uses \

#Unix/Linux File System
# - Case sensitive
# uses /

#Python Interpreter is smart enough to convert unix filepaths to windows filepaths
name = "\\dir\\file"
name = "/dir/file"
name = "c:/dir/file"
#These are all equivalent

#Python uses streams in order to work with data
#this allows you to work with files of unknown names
#Think of it like abstraction

# Files must be opened in a specific mode
#The options are : Read, Write, and update, or essentially both

#File Types
#Files can be either text streams or binary streams
#Text streams are like the current file lines of text
#Binary streams are other formats. Executables, pictures, videos, etc.
#These files need to be read byte by byte

#Here again is another issue of windows being bonkers legacy code
#Linux marks the end of aline with the LF, or ASCII code 10. In python this is read as:
"\n"
#Windows, as it is based off of a legacy system, uses LF and CR, or ASCII code 13. In python, this is read as:
"\r\n"

#This can create a sense of portability. A portable app in this sense works across multiple OSes
#Problem may be potentially overcome with the OS module and some prechecking

#The actual File Handling

#Python has a few way to open files
#stream = open(r'sample.txt', mode = 'w', encoding = 'UTF-8')
#stream.close
#This method uses storage of an object in main namespace. There is another way as well
with open(r'PracticeChallenges/Labs/Module8/Files/sample.txt', mode = 'r', encoding = 'UTF-8') as stream:
    pass
#this method automatically closes the file when one is done with the code.
#Both have there place.

#notice the syntax on the open() statement
#open('./sample.txt', mode = 'r', encoding = None)
#         file        file mode        text encoding
#this is the natural way to open *text* files

#There are 3 modes for opening files, and 2 modifier items


#r:
# - opens in read mode
# - file must exist, and has to be readable

#w:
# - opens in write mode
# - file doesn't need to exist
# - if the file doesn't exist it will be created
#   if the files does exist it will be overwritten

#a:
#Same as w, but places the cursor at the end of the file
#Doesn't erase data

# + modifier
# - works on the r and w keys
# allows both reading and writing

#b:
# - goes at the very end
# signifies a binary file

#Bonus:
#t:
# -opens the file in text mode
# - Automatically assumed


#how to properly open a file:

try:
    stream = open(r"C:\Users\User\Desktop\file.txt", "rt")
    # Processing goes here.
    stream.close()
except Exception as exc:
    print("Cannot open the file:")

#There are some streams we have by default, which are accessable through sys

#sys.stdin
# - standard input
# - Used for keyboard and input()

#sys.stdout
# - standard output
# - Associated with the screen
# - think print

#sys.stderr
# - standard error output
# - used for where errors should be sent
# - useful for separating useful output from errors

#remember to close your system with .close() if you didn't use with

#If you get an ir error, you may want to get the errno

#except IOError as exc:
#    print(exc.errno)

#You can reference this later in your code, or use it to dignose errors yourself
#If you want to do it right, you should get the strerror from os
from os import strerror

try:
    pass
except Exception as exc:
    print("The file could not be opened:", strerror(exc.errno))