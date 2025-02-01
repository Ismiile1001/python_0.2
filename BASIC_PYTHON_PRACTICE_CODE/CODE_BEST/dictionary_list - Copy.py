# marks = { 
#      "HI" : 0,
#      "kona ":100


# }

# #  method for dictionary

# print ( marks["HI"])
# print (marks.items())
# print ( marks.keys())
# print ( marks.values())
# marks.update({"HI" : 99})
# print (marks)




# ----------------------------------------------------------------  --------------------------------
# set 
# empty  set  
# s = set()
s =  { 1,5,68,86,434,3,5,5,5,5,5 }
s1 = (3,1,5,6,86,3)
print(s)
#  set  method 
# print(len(s))
# s.add(500)
# s.remove(68)
# print(s)
# kona = s.union(s1)
# kona2= s.intersection(s1)
# print( kona )
# print( kona2 )



# -------------------------------------------------------------------
#   practice 


# word = {
#      "bachao "  :  "help ",
#         "bilai" : "cat "
# }

# word1= input( " inter  your  words : ")
# print( word[word1] )



# store and perform the operations 

# s = set()

# v1 = int(input( " inter your value : "))
# s.add(v1)
# v2 = int(input( " inter your value : "))
# s.add(v2)
# v3= int(input( " inter your value : "))
# s.add(v3)
# v4 = int(input( " inter your value : "))
# s.add(v4)

# print ( s)


#  can we  store the value  like a string  -- ans is ; hobe 

# s = set() 
# s.add(input( " inter your value : "))
# s.add(input( " inter your value : "))

# print ( s) 


#  several valus 

# s = set() 
# s.add(1)
# s.add(1.0)
# s.add("1")
# print( s , len(s))


#  dec 


d = {}

name = input ( "inter your name :" )
lan = input ( " inter your lan :" ) 
d.update({name:lan})

name = input ( "inter your name :" )
lan = input ( " inter your lan :" ) 
d.update({name:lan})
print(d )
