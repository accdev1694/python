# While Loop Examples

# 01: ---> Age validation <---
# here we write a program to ensure the user types in an 
# age that is not a negative number or a decimal

age = input("What is your age? ")
# age must be a positive number
while not age.isdigit() or int(age) < 0:
    print("age must be a positive number")
    age = input("What is your age? ")
    
print(f"you are {age} yrs old")
    