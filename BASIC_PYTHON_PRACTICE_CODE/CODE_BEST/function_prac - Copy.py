#  find the grater number  input is 3  -- using  the  funtion
def get_grater(a,b,c):
    if a>b and a>c:
        print(f"{a} is a greter number ")
    elif  b>a and b>c:
        print(f"{b} is a greter number ")
    else:
        print(f"{c} is a greter number ")

n = int(input('first input : '))
y = int(input('2nd  input : '))
z = int(input('3rd  input : '))
get_grater(n,y,z) #  output : 5 is a greter number                


#  write  a program using fuction to convert  celsius to fahrenheit
#  recursion  for natural number 
 
def sum ( n ):
    if n == 1:
        return 1 
    else:
        return n + sum (n-1)
print(  sum(5))




#  again recurtion of fuction 
'''recurtion in pattern 
***
**
* 
'''

def pattern(n): 
    if n==0: 
        return
    else : 
        prnt('*' * n)  # print the current line of asterisks
        pattern(n-1) 
    
pattern(3)      


#  list in funrtion 




