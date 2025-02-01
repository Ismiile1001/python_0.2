
# 

my_list = [1,2,3,5,7]
new_list =[]
for item in my_list:
    new_list.append(item*item)
print(new_list)



# try it more esay way to slove -- it calls comprehension

new_list_comprehension = [item*item for item in my_list]
print(new_list_comprehension)


#  comprehension is more readable and efficient than traditional for loop.
