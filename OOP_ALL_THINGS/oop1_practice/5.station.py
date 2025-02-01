
from random import randint
class station:
    def __init__(self,train_no):
        self.train_no = train_no


    def ticket_book(self,name ):
        print( f" train no {self.train_no} is booked by  mr.{name}")

    def train_start(self,time):
        print(f" train no {self.train_no}  is start on the time of :{time} am")

    def train_fare(self, frm,to):
        print(f"the ticket fare train  no :{self.train_no} is go form {frm} to {to} is {randint(200,400)}"
    )

s1=station(2243)
s1.ticket_book("ismile")
s1.train_start(4)
s1.train_fare("dhaka","coxbazer")

