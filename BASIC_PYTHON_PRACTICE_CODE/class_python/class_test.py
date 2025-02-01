# map 

def square(x):
    return x ** 2
lis  = [1,2,3,4,5]

squared_list = list(map(square, lis))
print(squared_list)



def unregistered_student ():
    pass

def student_registration ():
    while True:
      field = input("Enter the field to submit (name) or 'exit' to stop: ")  
      if field == "exit":
        break  

    if field == "name":
        value = str(input("Enter  student_name (as str ): ")) 
        value = input(f"Enter {field} (max 5 characters): ")[:7] 
    student_registration[field] = value
print("Student Info Submitted:", student_registration)
     

