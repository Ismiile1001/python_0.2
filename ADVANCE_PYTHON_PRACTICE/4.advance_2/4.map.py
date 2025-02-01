#  for list all item 
l = [1,2,3,4,5,6]
square = lambda x:x*x 

# square korbo list ar all items 
sq_list = map(square,l)
print(list(sq_list))