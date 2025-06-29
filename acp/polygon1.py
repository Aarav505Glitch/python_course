from abc import ABC ,abstractmethod
class polygon(ABC):
    def area(self):
        pass
class triangle(polygon):
    def __init__(self,b,h):
        self.b,self.h=b,h
    def area(self):
        return 0.5 *self.b *self.h
class rectangle(polygon):
    def __init__(self,l,w):
        self.l,self.w=l,w
    def area(self):
        return self.l*self.w
shape=input("enter shape").lower()
if shape=='triangle':
    b,h=map(float,input("enter base and height").split())
    print("area: ",triangle(b,h).area())
elif shape =='rectangle':
    l,w=map(float,input("enter base and height").split())
    print("area: ",rectangle(l,w).area())
else:
    print("unsupported shape")




        
    