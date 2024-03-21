# files-> The data can be written, read and store
# There are 3 ways to access the data in a file
#1) Read mode (You can read the data )
#2) Write mode (You can write anything but it will erase if any data was present before )
#3) Append mode (You can update anythig without disturbing the previous data)

myfile=open("test.txt","r")   # r is for read method
print(myfile.read())  # myfile.read-> its a build in method in python to read a file
myfile.close()        #myfile.close() -> its use to close a file and it is neassary to close a file after use

myfile=open("test.txt","w") # w is for write method
print(myfile.write("This is written by the programmer \n")) # myfile.write-> its a build in method in python to write in a file

myfile=open("test.txt","r")
print(myfile.read())

myfile=open("test.txt","a")    # a is for append method
print(myfile.write("This is written by the user \n"))

myfile=open("test.txt","r")
print(myfile.read())


#Context manager-> it manages with the extra data like if some application is open it will close it for you

mylines=["Good evening \n", "Welcome back to the class"]

with open("test.txt", "w") as file:        # with -> it coloses the file after it is used so the it will not slow our system
  file.writelines (mylines)
  
with open("test.txt","r") as file:
  print(file.read())
  
  