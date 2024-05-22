# List Comprehension
mylist = [1,23,4,56,7,8,12,23,57,66,40,81]

odd = [i for i in mylist if i%2 != 0]
print(odd)

even = [i for i in mylist if i%2 == 0]
print(even)


# Dictionary Comprehension
mydict = {i:i**2 for i in mylist}
print(mydict)

# Set Comprehension
myset = {i for i in mylist if i%2 == 0}
print(myset)

# Generator Comprehension
def mygen(n):
    yield n-5+6
    yield n**2
    yield n-50
x = mygen(10)
print(x.__next__())
