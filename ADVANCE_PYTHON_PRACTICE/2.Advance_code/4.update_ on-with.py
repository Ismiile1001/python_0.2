
#  open multiple line 

with(
    open("file1.txt") as f1,
    open("file2.txt") as f2
):
    a=f1.readlines()
    print(a)

