n=int(input("enter a number"))
n_str=str(n)
n_digits=len(n_str)
sum_digit=sum(int(digit) ** n_digits for digit in n_str)
if n==sum_digit:
    print(f"{n} is an armstrong number")
else:
    print(f"{n}is not a armstrong number")
