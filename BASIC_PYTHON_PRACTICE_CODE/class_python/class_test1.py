
def unregistered():
 pass


student_info = {}  
while True:
    field = input("Enter the field to submit (name/age/course) or 'exit' to stop: ")  
    if field == "exit":
        break  
    if field == "name":
        value = input("Enter nmae(as str): ")
    else:
        value = input(f"Enter {field} (max 5 characters): ")[:5]  

    student_info[field] = value  
print("Student Info Submitted:", student_info) 





