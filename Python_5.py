def calc ():
  num1=int(input("Enter the first number"))
  num2=int(input("Enter the second number"))
  print("The sum of the two numbers is:",(num1+num2))
calc()

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

def a(name):
  print("hello",name)
a("tom")
def a(name):
  for i in range (10):
    print("hello",name)
a("tom")

# For loop -> its type of loop help us to print the data one by one
list1=[12,51,48,62,35] 
for x in list1:
  print("The values of the list are:",x)
for i in range (1,10):
  print("The square of ",i,"is ",i**2)
for a in range(2,5):
  for b in range(1,10):
    c=a+b
    print("The sum of two values are",c)

    
def calc():
  for a in range(5):
    for b in range(5):
      c=a+b
      a=int(input("Enter the value for a:"))
      b=int(input("Enter the value for b:"))
      print("The sum the two variables are",(a+b))
calc()



