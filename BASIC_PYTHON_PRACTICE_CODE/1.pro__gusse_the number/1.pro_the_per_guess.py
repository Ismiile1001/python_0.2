import random
n = random.randint(1,10)
a = -1
guessess = 0
while(a!=n):
    guessess += 1
    a = int(input(" Enter your guess : "))
    if (a > n):
        print(" guess the lower number \n ")
    else:
        print("guess  the higher number \n")    

print(f"The number   is finded and your guessess number is :  {guessess} " )        