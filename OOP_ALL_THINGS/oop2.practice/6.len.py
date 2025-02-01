class vector:
    def __init__(self,l) :
        self.l=l


    def __len__(self) :
        return len(self.l)   


s1 = vector([1,2,3,4,6])
print(f"the len of list is :",{len(s1)})