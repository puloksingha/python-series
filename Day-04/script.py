#Control Flow (if/else)
#If statement
age = 18
if age >= 18:
    print("You are an adult.")
#If-else statement
age = 16
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")   
#If-elif-else statement
age = 65
if age < 18:
    print("You are a minor.")
elif age < 65:
    print("You are an adult.")  
else:    print("You are a senior citizen.") 


# Logical Operators
#And operator
age = 25
if age >= 18 and age < 65:
    print("You are an adult.")  
#Or operator
age = 70
if age < 18 or age >= 65:
    print("You are not an adult.")  
#Not operator
age = 15 
if not age >= 18:
    print("You are a minor.")
    
    