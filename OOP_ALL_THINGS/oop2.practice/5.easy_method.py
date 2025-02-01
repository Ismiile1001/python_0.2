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
        
