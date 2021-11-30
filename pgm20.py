evenList =[4,11,22,33,15,8,9,10]
print("List Items = ", evenList)

for ev in evenList:
    if (ev % 2 == 0):
        evenList.remove(ev)
    
print("List Items after removing even Items = ", evenList)
