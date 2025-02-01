
# this is called global variable --> we used it all plase 
a=45
b= 10

def test():
    #  this is local variable
    # when we need to change the global variable
    #  ata ter  nijer 
    global a
    b=20
    a=3
    print(a)
    print(b)


# testing 
# mone rakhte hobe --> baire lok bairer e  
test()
# local  -- print  hoise 
print(b)

