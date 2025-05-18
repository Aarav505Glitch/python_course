def fact(n):
    if n==1:
        return n 
    else:
        return n*fact(n-1)
num=int(input("enter number"))
if num<0:
    print ("no factorial for negitive number")
elif num ==0:
    print("factorialof zero is one")
else :
    print("the factorial is ",fact(num))
