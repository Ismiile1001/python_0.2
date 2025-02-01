class towdvector: 
    def __init__(self,i,j):
        self.i=i
        self.j=j

    def show(self):
        print(f"the vector is a : {self.i}i + {self.j}j")    


class threedvector(towdvector): 
    def __init__(self,i,j,k):

        #  (super method) -- ager class thaika ja ja lagbo ta used  kortasi  
        super().__init__(i,j)
        self.k=k

    def show(self):
        print(f"the threedvector is a : {self.i}i + {self.j}j +{self.k}k")    



s1 = towdvector(1,2)        
s1.show()

s2= threedvector(2,3,5) 
s2.show()