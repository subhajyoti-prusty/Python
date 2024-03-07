#set -> Unordered collection of data's,{},immutable,does't contain a duplicate value, can't use index, it's also mutiable

Set1={1,2,3,54,5,4,5,0}
print("The values of Set1 is ",Set1)
#print(Set1[2])        # See as here we can't use index values

#Add  (In sets if you want to add data use .add method)
Set1.add(False)
print(Set1)

# Union() -> It's use to combine the values/elements of sets
Set2 = {1,2,"ABC",4,5,6,7,False,9,114.32} 
Set3=Set1.union(Set2)
print(Set3)

Set4={56,564,31,256,15,31,2}
Set5=Set1|Set2|Set3|Set4      # This | also stands for union

# Intersection -> Shows the elements that are common
Set6=Set1.intersection(Set2)
print(Set6)

Set7=Set2&Set3&Set4          # This & also stands for intersection
print(Set7)

# clear-> to remove all the element of the set
Set1.clear()
print(Set1)

# Converting Sets from immutable to mutable
a=frozenset(["E","F"])
print(a)