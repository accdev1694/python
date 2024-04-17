# While some condition is true, some code gets executed over and over 
# until the condition changes to false

# lets get some user input and illustrate this:

gpa = input("what is your gpa: ")
print(f"your gpa is {gpa}")
# this is a simple program, but we can add some functionality to it

# lets add a validation to ensure user types in something     
preffered_color = input("what is your color: ")
if preffered_color == "":
    print("you did not type in anything")
    
else:
    print(f"your preffered color is {preffered_color}")
# if this program sees an empty string, it tells the user 
# that they didnt type anything, and the exits

# we can add some more functionality to this program
# lets continue to prompt the user to type in something, if they didnt before
email = input("What is your email? ")

while email == "":
    print("this field cannot be empty!")
    email = input("What is your email? ")
    
print("Your email is", email)                   # another way to display a variable along with some text
    