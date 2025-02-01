class library:
    @staticmethod
    def library():
      print( "YOU WILL FIND ALL KIND OF BOOK HERE ")

class historical_book:
    def Nobab(self):
        name = "BANGLA LAST NOBAB"
        print(f"all about (Nobab) the book name is :{self.name}  ")

    def PAKISTAN(self):
        name = "KILL -- BANGLADESHI"
        print( f" all about (pakistani--dictator) the bookk name si :{self.name} ")

class biology:
    @staticmethod
    def bio(self):

       print ("all type of biology book you see in this class  !!! ")


class economical:
    @staticmethod
    def world():
        print("have no dollars")


# multiple inheritance  --- all in  one 

class all_book(library,historical_book,biology,economical):
    @staticmethod
    def all_book():
      print("all done")




#  object 
s1 = all_book()
s1.all_book()
s1.world()














        