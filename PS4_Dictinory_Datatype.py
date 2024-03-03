# Dictinory -> Its consist of key and values,{},

mydic={
    "Usearname":"Admin",
    "Password":123,
    "Brand":"Lenovo"
}

print(mydic)

print(mydic['Usearname'])     # In the square bracket you enter the key and it will show you the value of the key

#Update
mydic['Usearname']= "Me"      # You can change the values with the help of the key only not through index value
print(mydic)

#Add single value
mydic['Yearofmake']= "2023"
print(mydic)

#Add multipule values
mydic['Brand']= ["a","b","c"]
print(mydic)

# Adding a list to a dictinory
lsit1 = [1,"bhca",3.260,4]
mydic['List']=lsit1
print(mydic)

#Remove a value
mydic.pop("Brand")
print(mydic)

#Delete the whole dictinory
del mydic
print(mydic)
