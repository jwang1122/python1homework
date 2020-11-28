"""
Area and perimeter
"""
import math 
def   circlecalculate(*args, unit='in'):

    radius=args[0]
    if unit=='feet':
        radius=12*radius
    area=math.pi*radius**2
    perimeter=2*math.pi*radius
      
    return (area,perimeter)


(area,p)=circlecalculate(1)
print("The first circle's area is %f in inches." % area)
print("It's perimeter is %f in inches." % p)
(area,p)=circlecalculate(1, unit="feet")
print("The second circle's is %f in inches." % area)
print("It's perimeter is %f in inches." % p)

def   rectangularORbox(*args):
    if len(args)<=1:
        return "Error"
    elif len(args)==2:
        print('The area of the rectangle:')
        return  args[0]*args[1]
    elif len(args)==3:
        print('The volume of the box:')
        return args[0]*args[1]*args[2]
    else:
        return  "Error, please put less than 4 arguments"


print(rectangularORbox(1))
print(rectangularORbox(1,2))
print(rectangularORbox(1,2,3))
print(rectangularORbox(1,2,3,4))