n = int(input("enter a number"))
a,b=0,1
print("fibonacciseries:")
for i in range (n):
    print(a,end=" ")
    a,b=b,a+b