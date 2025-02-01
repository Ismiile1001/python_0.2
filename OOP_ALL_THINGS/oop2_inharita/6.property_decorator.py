class total_mark:
    def __init__(self,math,bangla,english):
        self.math = math
        self.bangla =bangla
        self.english =english

#  this is a property of--- (init) --
    @property
    def avarage(self):
        return ((self.math+self.bangla+self.english)/3)


# object

s1 = total_mark(100,100,100)
print(s1.avarage)

#  auto update hoye jabe 
s1 = total_mark(100,60,100)
print(s1.avarage)