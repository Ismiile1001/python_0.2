#  tell the types  of  any things 
#  you can import any type of (typer) for better understanding .. for examle 

from typing import List, Dict , String ,Tuple,Union

# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]

# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)

# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}

# Union type for variables that can hold multiple types
identifier: Union[int, str] = "ID123"




n : int = 4

nmae : str = " ismile"

def sum(a : int, b : int) -> int : 
    return a + b

# practice : 

#  best practice  .. bojano holo jah aii jaygai (int + str )  -> shod  ase 
number_string  : List[int,str] = [1,2,3,4,"kona -> str"]

name : List[str] = ["kona ", "ismile"]

not_changeable : Tuple[str,int] = ("kona ", "ismile ", 2,4,5)




