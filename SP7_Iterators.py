# Iterators-> an object that contains a countable number of values
list=[12,51,48,62,35]
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])

# Methods used to do iterators are "iter" and "next"
#iter- It will help you to pass the value. Eg:- i have a list and i just want to get the same values of the list without writting it
list=[12,51,48,62,35]
myiteration=iter(list)

# next method is used to print the values one by one
print(next(myiteration))

str1="Subhajyoti"
str_iteration= iter(str1)
print(next(str_iteration))
print(next(str_iteration))
print(next(str_iteration))
print(next(str_iteration))


