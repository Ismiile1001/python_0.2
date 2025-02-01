#  we used it for -------  constructor 
# used  for access other -- --- constructor 

class employees:
    # build a constructor
    def __init__(self):
        print("Constructing employees")
    a=1 




class programer(employees):
    def __init__(self):
        print("Constructing programer")
    b=3




# programer inside  the (manager)
# and (programer)-- class is a preant class of (manager)-- class
class manager(programer): 
    def __init__(self):
        super.__init__(self)
        print("Constructing manager")
    c=4





# object------
# all comes inside the (manager)
# s1=employees()
# print(s1.a)


# s1=programer()
# print(s1.b,s1.a)


s1=manager()
print(s1.a,s1.b,s1.c)