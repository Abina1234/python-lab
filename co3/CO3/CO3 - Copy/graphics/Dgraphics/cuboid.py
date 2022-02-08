def cuboid(x,y,z):
    a=2*((x*y)+(y*z)+(x*z))
    p=4*(x+y+z)
    print("Perimeter of cuboid:",p)
    print("Area of cuboid:",a)
l=int(input("Enter length of cuboid:"))
b=int(input("Enter breadth of cuboid:"))
h=int(input("Enter height of cuboid:"))
cuboid(l,b,h)
