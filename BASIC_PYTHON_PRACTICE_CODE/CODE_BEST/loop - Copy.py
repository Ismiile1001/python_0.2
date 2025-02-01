# loop 
i=0
for i in range(1,1000000000000000000):
    print (i,". i love python ")
    if i==10:
        break



 # while loop 
i = 0 
while i <= 10:
    
    print(i)
    i+=1





 #list =  using the loop 
 # ok go than 


l = [ "kona ", 1, "ismile "]
i=0 
while i < len(l):
    print(l[i])
    i=i+1







#  same  using the  for loop 


l = [ "kona ", 1, "ismile "]
for i in l :
    print ( i)






#  loop in string 

l = " kona "
for i in l :
    print ( i , end = " " ) 
else :
    print ( "done for today " )






#  BRACK 

for  i in range (1 ,100): 
    if  (i == 50):
         break 
    print (i)






    #  continue -- it  skip  50 
for  i in range (1 ,100): 
    if  (i == 50):
         continue 
    print (i)




    #  pass -- print  e hoibo nah 

for i in range (1,10): 
    print( i)
    pass    

for i in range (1,10): 
    print( i)



#  -------------------------------------------------------------------------------------------------

#  problem ------ multiplecation table using f string  

n = int (input(" inter  your  value :" ))
for i in range (1,11): 
    print( f"{n} X {11-i} = {(11-i) * n}") 
    
    # print( f"{n} X {i} = { i* n}") -- forword multiplication





#  strat with -- s ( print  it ) -- also  used f-string 

l = ["kona ", "shoel", "shohag", "mimi"]
for i in l:
    if(i.startswith("s")):
        print(f"hello {i}")





  # prim number  
n = int (input(" inter your value :" )) 
for i in range (2 , n):
    if n % i == 0:
        print(f"{n} is not a prime number")
        break
else:
    print(f"{n} is a prime number")

 




# prim number convert in to a while  loop

n = int (input(" inter your value :" )) 
i = 2
while i < n:
    if n % i == 0:
        print(f"{n} is not a prime number")
        break
else:
    print(f"{n} is a prime number")
    




# find the sum of natural number  


n = int (input(" inter your value :" )) 
sum = 0
i = 1
while (i <= n):
    sum = sum + i
    i = i + 1
print(sum)  
 



#  factorial convert

n = int (input(" inter your value :" )) 
factorial = 1
i = 1
while (i <= n):
    factorial = factorial * i
print(factorial)    


