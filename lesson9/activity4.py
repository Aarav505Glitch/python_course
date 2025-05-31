class parrot:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sing(self,song):
        return "{} signs {}".format(self.name,song)
    def dance(self):
        return "{} dances ".format(self.name)
blue=parrot("blue",10)
print(blue.sing("happy"))
print(blue.dance())
        
