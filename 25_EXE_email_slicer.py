# we create a program to slice an email collected 
# from a user into username and domain name

# collect user email:
email = input("type in your email:")

# find username:

username = email[:email.index("@")]
domain_name = email[email.index("@") + 1:]

print(f"your username is {username} for the domain name: {domain_name}")