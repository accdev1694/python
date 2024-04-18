# Email Validator Exercise
# here we create an application to test the input for an email 
# and ensure it is indeed an email format

email = input("enter your email:")

while not "@" in email:
    email = input("enter a valid email:")
    
domain = email[email.index("@"):]

print(f"your email is ****{domain}")