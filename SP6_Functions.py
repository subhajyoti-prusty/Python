# Functions -> A set of data will be executed whenever we call it
print("Hello and good evening")
print("Thank You")

def a():    # It is the indentation of a function    def a():
  print("Hello and good evening everyone ")
  print("Thank You all")

a()
a()
a()
a()

def name(): 
  a="Subha"
  print("My favorite student is",a)
# If you call the function inside the function then it will be a infinite loop
name()
name()
name()
name()
name()

def add(a,b): # Here a and b are parameters....... and parameters are nothing but is like variables and wu can store values in it
    c = a + b 
    print("The sum of",a,"and",b,"is",c)
add(5,6)
add(10,20)

def calc ():
  num1=int(input("Enter the first number "))
  num2=int(input("Enter the second number "))
  print("The sum of the two numbers is:",(num1+num2))
calc()
