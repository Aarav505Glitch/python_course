class student:
    grade=10
    name="aarav"
    def introduction(self):
        print("hii i am a student ")
    def details(self):
        print("my name is ",self.name)
        print("i study in grade",self.grade)
ob=student()
ob.introduction()
ob.details()