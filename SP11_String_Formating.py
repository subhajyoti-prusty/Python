# String Formating in Python
    # % operator
print("Hekko %s all %s" % ("World", "around"))

    # .format() method
print("Hello {} all {}".format("World", "around"))
print("Hello {1} all {0}".format("World", "around"))

    # F-Strings:- It converts the int,float,boolean to string type so that we can write it easily
score = 0
height = 1.8
IsWinning = True
print("Your Score is "+str(score))
print(f"Your Score is {score} , Your height is {height} and You are winning is {IsWinning}")

    # String Template Class
from string import Template
t = Template("Hello $name")
print(t.substitute(name = "World"))