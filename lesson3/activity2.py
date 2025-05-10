height=float(input("enter your height"))
weight=float(input("enter your weight"))

bmi=weight/(height/100)**2
print("your bmi is ",bmi)
if bmi<=18.4:
    print("your under weight ")
elif bmi<=24.9:
    print("you are healthy")
else:
    print("you are over weight")