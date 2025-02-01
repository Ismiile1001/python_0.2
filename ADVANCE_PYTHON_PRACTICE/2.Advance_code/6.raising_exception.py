#  for example 

a = int(input("Enter a number :"))
b = int(input("Enter 2nd number :"))



if (b == 0):
    raise ZeroDivisionError(" please enter a integer number other wise the program will not run \n ")
else:
    print("the number is : ", a/b)


