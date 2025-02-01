class calculater:
    def __init__(self,n):
        self.n = n
    def square(self):
        print(f"squre is: {self.n * self.n}")    
    def cube(self):
        print(f"cube is: {self.n * self.n * self.n}")    
    def squareroot(self):
        print(f"squareroot is: {self.n**1/2}")    

s1 = calculater(int(input("inter your value : ")))
s1.squareroot()
s1.cube()
s1.square()   


        