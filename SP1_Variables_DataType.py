# Variables-> Which stores the value
'''_num1_,num,Num,Num1,'''

# String-> set is a set of characters written in a single or double quotation
name='Subha'
print(name)

_a_="Hello all"
print(_a_)
print(type(_a_))

#Int-> a number without a decimal value
num1=10
num2=20
print(num1+num2)
print(type(num1))

#Float-> a number with decimal value
num3=34.45
num4=63.89
sub= num3-num4
print(sub)
print(type(sub))

num5=30
num6=38.6
add=num5+num6
# Concatenation-> combining the data
print('The additin of num5 and num6 is :',add)
print('The values are',add,"\n total")
print(type(add))

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

score = 0
height = 1.8
IsWinning = True

# F-Strings:- It converts the int,float,boolean to string type so that we can write it easily

print("Your Score is "+str(score))
print(f"Your Score is {score} , Your height is {height} and You are winning is {IsWinning}")

