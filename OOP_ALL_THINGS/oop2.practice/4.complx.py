
#  aktu  bojte  hobe 

# class complex:
#     def __init__(self,r,i):
#         self.i= i
#         self.r=r

#     def __add__(self,c2):
#         return complex(self.r + c2.r , self.i + c2.i)
    
#     def __str__(self):
#         return f"{self.r} + {self.i }i"
    

# self = complex(2,3)    
# num2 = complex(3,4)

# print(self + num2)



# simple  way to solve a complex problem


class complex:
    def __init__(self,img,real):
        self.img = img
        self.real = real

    def show(self):
        print(self.real,"i +",self.img,"j")



# create a function to add a complex number
    def add(self,num2):
        newreal = self.real + num2.real
        newimg= self.img + num2.img
        return complex(newreal,newimg)





num1=complex(2,3)
num1.show()

num2 = complex(4,3)
num2.show()

ok = num1.add(num2)
ok.show()