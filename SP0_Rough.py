mylist = [1,23,4,56,7,8,12,23]
evenlist=[]
oddlist=[]

for i in mylist:
    if i%2 == 0:
        evenlist.append(i)

for i in mylist:
    if i%2 != 0:
        oddlist.append(i)
        
print(evenlist)
print(oddlist)