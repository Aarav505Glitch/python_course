import random
s_num=random.randint(1,10)
print("welcom to the number guessing game")
while True:
    try:
        guess=int(input("enter your guess"))
        if guess <s_num:
            print("too low , try again")
        elif guess >s_num:
            print("too high,try again")
        else:
            print("congratulation,you guessed it right" )
            break
    except ValueError:
        print("enter a valid number")
