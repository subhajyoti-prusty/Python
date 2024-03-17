# files-> The data can be written, read and store
# There are 3 ways to access the data in a file
#1) Read mode (You can read the data )
#2) Write mode (You can write anything but it will erase if any data was present before )
#3) Append mode (You can update anythig without disturbing the previous data)

myfile=open("test.txt","r")   # r is for read method
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