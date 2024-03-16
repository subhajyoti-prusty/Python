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