
#  multilevel inheritance 


class employees:
    a=1 

class programer(employees):

    b=3

# programer inside  the (manager)
class manager(programer): 
    c=4


# all comes inside the (manager)
s1=employees()
print(s1.a)


s1=programer()
print(s1.b,s1.a)


s1 = manager()
print(s1.a,s1.b,s1.c)
    