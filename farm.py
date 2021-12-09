farm={"sheep":5,"cow":2,"goat":10}
print("Elements in dictionary:",farm)
d={"duck":8}
farm.update(d)
print("Elements in dictionary after update:",farm)
c=len(farm)
print("No:of items in dictionary:",c)
del(farm['cow'])
print("Elements in dictionary:",farm)