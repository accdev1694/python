# here we validate user's password and check for the following:
    # between 6 and 10 characters long
    # contains a number
    # contains capital
    # contains a special character or symbol
    
password = input("Enter a password. (must be 6-10 char long, must contain at least a number, capital and a special char): ")
special_char = "!@#$%^&*()-_+=~`[]{}|;:,.<>?/'\"\\"

# conditions
if len(password) < 6:
    print("password too short! must be more 6 or more characters long")
    
elif len(password) > 10:
    print("password too long! must not be more than 10 character long")
    
elif not any(char.isdigit() for char in password):
    print("must contain at least one number")
    
elif not any(char.isupper() for char in password):
    print("must contain at least one uppercase characters")
    
elif not any(char in special_char for char in password):
    print("must contain at least one special character")
    
else:
    print(f"password successfully created: {password}")
    
