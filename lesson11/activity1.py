class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"cat name is {self.name},and the cat is {self.age} years old")
    def sound(self):
        print("meow")
class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"dog name is{self.name},and the dog is{self.age}years old")
    def sound(self):
        print("bark")
cat1=cat("cat",2.6)
dog1=dog("dog",3.4)
for animal in (cat1,dog1):
    animal.sound()
    animal.info()