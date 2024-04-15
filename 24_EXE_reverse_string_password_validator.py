# as a measure to ensure a password is not easily guessed, 
# lets create a validation to guard against this

# collect user password:
user_name = input("what is your username")
password = input("Type in your password:")

# reverse validation
if password == user_name[::-1]:
    print("Weak password!!! Type in a strong password")
    
else:
    print(f"Dear {user_name} your password is: ***{password[-2:]}")
    
