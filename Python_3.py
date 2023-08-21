# Dictinory -> Its consist of key and values,{},

mydic={
    "Usearname":"Admin",
    "Password":123,
    "Brand":"Lenovo"
}
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

#Remove a value 
mydic.pop("Brand")
print(mydic)

#Delete

del mydic
print(mydic)

#set -> Unordered collection of data's,{},immutable,does't contain a duplicate value, can't use index, it's also mutiable 
 
Set1={1,2,3,54,5,4,5,0}
print("The values of Set1 is ",Set1)
#print(Set1[2])        # See as here we can't use index values

#Add  (In sets if you want to add data use .add method)
Set1.add(100)
print(Set1) 

Set2={345.6,7,345,True,'Data',2}

# Union() -> It's use to combine the values/elements of sets
Set3=Set1.union(Set2)
print(Set3)

Set4={56,564,31,256,15,31,2}
Set5=Set1|Set2|Set3|Set4      # This | also stands for union
print(Set5)

# Intersection -> Shows the elements that are common
Set6=Set1.intersection(Set2)
print(Set6)

Set7=Set2&Set3&Set4          # This & also stands for intersection
print(Set7)

# clear-> to remove all the element of the set 
Set1.clear()
print(Set1)