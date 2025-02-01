
# first qustion 


english= int(input(" enter your  number the  program say that you rae pass or not : "))
math= int(input(" enter your  number the  program say that you rae pass or not : "))
bangla = int(input(" enter your  number the  program say that you rae pass or not : "))

total = (english + math + bangla)/300
if (total>=40 or english >=33 or math >= 33 or bangla >=33):
    print("your are  pass in exam  ", total)
else:
    print("your are fail in exam ",total)     



# spam  massage detection 

p1= " i give yor a car"
p2= "GIVE ME YOUR PHONE NUMBER"
p3 ="hi kona"
 
massage = input( "chack the massage : ")


if ((p1 in massage) or (p2 in massage) or (p3 in massage) ):
    print("spam message ")
else: 
    print("not spam message ")    





#your  name  less than 10 characters or not   

name = input("enter your name : ")

if len(name) < 10 :
    print("your name is less than 10 characters ")
else:
    print("your name is 10 characters or more ")




# find that your  name  in the list or not  in the  list 
l  = [" kona ", "ismile ", " sadat "]
name = input("enter your name : ")

if name in l:
    print("your name is in the list ")
else :
    print("your name is not in the list ")





 # using the grade  variable to find your  grade  

marks = int(input ("inter your marks : ")) 

if marks <=100 and marks >= 90 :
    grade = "Ex"    
elif marks <90 and marks >=80:
    grade = "A+"
else:
    grade="fail "
print( " yourv grade  is : ", grade )        




#  chack your  post  

post = input("enter your post : ")

if ("kona".lower()  in post.lower()): 
    print( "this talking about  :  kona ")
else : 
    print(" nothing ")    