#  shorashori  calss --  attributes used korte parbo -- instance attributes thaka shorteo--


class number:
    a=1
    @classmethod
    # self -- er jaygai -- cls ---chole tai instance attributes kaj kore nah 
    def num(cls):
        print(f"the number is : {cls.a}")



# instance attributes thaka shorteo -- calss attributes dekahbe
s1 = number()        
s1.a = 4 
s1.num()