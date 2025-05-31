class parrot:
    animal="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
blue=parrot("blue",10)
green=parrot("green",15)
print("blue is a {}".format(blue.animal))
print("green is a {}".format(green.animal))
print("{}is {} years old".format(blue.name,blue.age))
print("{}is {}years old".format(green.name,green.age))
