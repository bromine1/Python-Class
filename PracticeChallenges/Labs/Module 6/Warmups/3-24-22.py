#Ryan Stauffer 3-24-22 Warmup

#1. Demonstrating the strip() method:
print("[" + "   aleph   ".strip() + "]")

#Will remove the leading and trailing whitespace

#2. Demonstrating the strip() method by removing spaces at the beginning and at the end of the string:

txt = "     cherry     "
x = txt.strip()
print("believe me of all fruits", x, "is my favorite")
#"believe me of all fruits", cherry, "is my favorite"

#3. Demonstrating the strip() method by removing the leading and trailing characters:

txt = ",,,,,ssttgg.....cherry....sss"

x = txt.strip(",.gst")

print(x)
#Will print "cherry"

str1 = " the Champions of NCAA will be known as the best of the best in the entire world"
str1 = str1.strip(" the")
# remove the
print (str1)
#remove somethign else
str1 = str1.strip("Champions")
print (str1)

str2 = " the best way to learn programming is be the best at practicing the examples daily"
str2 = str2.strip(" the") #remove the
print(str2)
str2 = str2.strip("best") #remove something else
print(str2)

str3 = " the teacher can be the greatest if the opportunity to teach daily is present"
str3.strip(" the") # remove the
print(str3)
str3.strip("teacher") #remove something else
print(str3)