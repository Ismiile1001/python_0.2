class employees:
    salary = 280
    increment = 19

#  akhane increment -- return korte parbo -- property decorator er karone 
    @property
    def increament_after_salary(self):
        return self.salary + self.salary *(self.increment/100)
    
    # @increament_after_salary.setter
    
    




s1 = employees()
print(s1.increament_after_salary)