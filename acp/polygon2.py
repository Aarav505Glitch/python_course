class polygon:
    def area (self):
        pass
class triangle(polygon):
    def __init__(self,base,height):
        self.__base=base 
        self.__height=height
    def area (self):
        return 0.5*self.__base*self.__height
class rectangle(polygon):
    def __init__(self,length,width):
        self.__length=length
        self.__width=width
    def area (self):
        return self.__length*self.__width
def get_shape():
    shape=input("enter a shape(rectangle/triangle)").lower()
    if shape=="triangle":
        b,h=map(float,input("enter base and height").split())
        return triangle(b,h)
    elif shape=="rectangle":
        l,w=map(float,input("enter length and breadth").split())
        return rectangle(l,w)
    else:
        return None
shape=get_shape()
if shape :
    print("area:",shape.area())
else:
    print("invalid shape")




    
