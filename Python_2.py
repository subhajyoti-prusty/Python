# Boolean -> it provides two condition true or false 
print(2>3)

a=10
b=int('10')
print(a>=b)
# we use double equal (==) to compire the data type 
print(a==b)

num1=int(input("Enter the 1st value:"))
num2=int(input("Enter the 2nd value:"))
add=num1+num2-num1*num2
print("The values are:",add)

from IPython.core.formatters import pretty
# List-> ordered collection of datatype ,[],mutable
mylist=[1,'data',True,45.03,"details"]
print(mylist)
# Index number-> helps to print individual data 
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[3])
print(mylist[4])

# Update
mylist[-3]=False
print('After updating the value is ',mylist)

# Append -> If you want to add values to the list 
mylist.append(100)
print('After appending the value is ',mylist)

# Insert  ->when you want to add vale in some specific place of a the list
mylist.insert(3,100)
print('The value are ',mylist)

# Delete -> To remove some value
del mylist[-1]
print('The value are ',mylist)

# Remove-> removes the value from the left side
mylist.remove(100)
print('The value are ',mylist)

#pop-> Remove value like delete but using index number
mylist.pop(0)
print('The value are ',mylist)

#Extend -> to insert more than one value
mylist1=[60,59,18,47]
mylist.extend(mylist1)
print(mylist)

print(type(mylist))
print(len(mylist))

# Tuple-> ordered collection of datatype,(),immutable
mytuple=("Data",1,33.4,'Task')
print(mytuple)