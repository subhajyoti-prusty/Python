#Modules->extension containing Python code that can be imported inside another Python Program
# Math-> consist of all mathematical operations
import math
print(math.sin(1))
print(math.factorial(4))
print(math.pi)
print(math.sqrt(4))

# datetime-> Gives the date and time
import datetime
x=datetime.datetime.now()
print(x)

# random: it is used to generate randon functions

import random
print(random.randint(0, 5))
import random
print (random.randint(0, 5)) #it will give random data is present in ranges to 5 when we run code.

List=[1,2,True, 115, "hello", "abh"]
print(random.choice(List)) #it will give randon data is present in list when we run code

#slicing -> range of data can be printed
s="python"
print(s[0:2]) #will print upto on index lower
print(s[:3])
print(s[3:])

# files-> The data can be written, read and store
# There are 3 ways to access the data in a file
#1) Read mode (You can read the data )
#2) Write mode (You can write anything but it will erase if any data was present before )
#3) Append mode (You can update anythig without disturbing the previous data)

myfile=open("a.txt","r")   # r is for read method
print(myfile.read())  # myfile.read-> its a build in method in python to read a file
myfile.close()        #myfile.close() -> its use to close a file and it is neassary to close a file after use
myfile=open("a.txt","w") # w is for write method
print(myfile.write("This is written by the programmer \n")) # myfile.write-> its a build in method in python to write in a file
myfile=open("a.txt","r")
print(myfile.read())
myfile=open("a.txt","a")    # a is for append method
print(myfile.write("This is written by the user \n"))
myfile=open("a.txt","r")
print(myfile.read())
#Context manager-> it manages with the extra data like if some application is open it will close it for you

with open("a.txt","r") as file1:     # with -> it coloses the file after it is used so the it will not slow our system
  print(file1.read())

  mylines=["Good evening \n", "Welcome back to the class"]
with open("a.txt", "w") as file:
  file.writelines (mylines)
with open("a.txt","r") as file:
  print(file.read())
