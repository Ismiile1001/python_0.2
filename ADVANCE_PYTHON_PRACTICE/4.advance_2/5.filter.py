
# filter korte lage ayta 
l = [1,2,3,4,5,6]
def even(n):
    if(n%2 == 0):
        return True
        return False
new_list = filter(even, l)    
print(list(new_list))
