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