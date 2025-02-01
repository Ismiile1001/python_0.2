#  using the  while loop  for i/o
f = open("kona.txt", "r")
line = f.readline()
while line  != (""):
    print(line , end = "")
    line = f.readline()