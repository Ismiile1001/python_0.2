class employees:
    def __init__(self,name,salary,language):
        self.name = name
        self.salary = salary
        self.language = language
        print("All done !")

s1 = employees("ismile",10000000000,"python")        
print(s1.name,s1.salary,s1.language)

s2 = employees("kona",10000000,"java")
print(s2.name,s2.salary,s2.language)