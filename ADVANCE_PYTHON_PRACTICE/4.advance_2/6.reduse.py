
from functools import reduce
l = [1,2,3,4,5,6]
def sum(a,b):
    return a+b
n_list=reduce(sum,l)
print(n_list)
