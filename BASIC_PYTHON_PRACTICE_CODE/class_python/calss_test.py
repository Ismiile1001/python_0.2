# def generate_password(s):
#     if len(s) == 10:
#         return   s[-3:].lower()+s[:3].upper() +'!@#$' 
        

# s = input("Enter the string to generate password: ")
# print(generate_password(s))







vowels = 'aeiouAEIOU  ' 



count = 0  
text = input("Enter a string: ")[:5]


for char in text:
    if char in vowels:
        count += 1  
        print("Number of vowels:", count)
    else :
        print("Number of consonants:", len(text) - count)
        break