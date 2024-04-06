list = [2,4,5,8,7,9,12]

# Here the index is within the range of the list so it will print the value at index 5
try:
    print(list[5])
except:
    print("Index given is out of boundry of list")
    
# Here the index is out of the range of the list so it will print the message "Index given is out of boundry of list"
try:
    print(list[10])
except:
    print("Index given is out of boundry of list")

    
num1 = 10
num2 = 0
try:
    print(result = num1/num2)
except:
    print("Division by zero is not allowed")    
    
try:
    x = open("a.txt",r)
    print(x.read())
except:
    print("File not found")
finally:
    print("This is the finally block")
    
try:
    print("HELLO") 
except:
    print("File not found")
finally:
    print("This is the finally block")